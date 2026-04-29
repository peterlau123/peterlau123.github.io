---
title: Triton Fused Softmax Kernel 
subtitle: '学习与思考'
layout: post
author: peter_lau
published: true
categories:
- AI
tags:
- AI
- Engineering
toc: true
mermaid: true
date: 2026-04-28 00:23:14 +0800
---

本文代码来自[triton-02-fused-softmax](https://triton-lang.org/main/getting-started/tutorials/02-fused-softmax.html)。

<mark style="background-color: yellow;">Triton的样本代码实现基于假设：**每一行数据可以完整的放入GPU的shared_memory中**</mark>

## kernel外围驱动代码

### 样本代码

```python
properties = driver.active.utils.get_device_properties(DEVICE.index)
NUM_SM = properties["multiprocessor_count"]
NUM_REGS = properties["max_num_regs"]
SIZE_SMEM = properties["max_shared_mem"]
WARP_SIZE = properties["warpSize"]
target = triton.runtime.driver.active.get_current_target()
kernels = {}

def softmax(x):
    n_rows, n_cols = x.shape

    # The block size of each loop iteration is the smallest power of two greater than the number of columns in `x`
    BLOCK_SIZE = triton.next_power_of_2(n_cols)

    # Another trick we can use is to ask the compiler to use more threads per row by
    # increasing the number of warps (`num_warps`) over which each row is distributed.
    # You will see in the next tutorial how to auto-tune this value in a more natural
    # way so you don't have to come up with manual heuristics yourself.
    num_warps = 8

    # Number of software pipelining stages.
    num_stages = 4 if SIZE_SMEM > 200000 else 2

    # Allocate output
    y = torch.empty_like(x)

    # pre-compile kernel to get register usage and compute thread occupancy.
    kernel = softmax_kernel.warmup(y, x, x.stride(0), y.stride(0), n_rows, n_cols, BLOCK_SIZE=BLOCK_SIZE,
                                   num_stages=num_stages, num_warps=num_warps, grid=(1, ))
    kernel._init_handles()
    n_regs = kernel.n_regs
    size_smem = kernel.metadata.shared
    if is_hip():
        # NUM_REGS represents the number of regular purpose registers. On CDNA architectures this is half of all registers available.
        # However, this is not always the case. In most cases all registers can be used as regular purpose registers.
        # ISA SECTION (3.6.4 for CDNA3)
        # VGPRs are allocated out of two pools: regular VGPRs and accumulation VGPRs. Accumulation VGPRs are used
        # with matrix VALU instructions, and can also be loaded directly from memory. A wave may have up to 512 total
        # VGPRs, 256 of each type. When a wave has fewer than 512 total VGPRs, the number of each type is flexible - it is
        # not required to be equal numbers of both types.
        NUM_GPRS = NUM_REGS
        if is_cdna():
            NUM_GPRS = NUM_REGS * 2

        # MAX_NUM_THREADS represents maximum number of resident threads per multi-processor.
        # When we divide this number with WARP_SIZE we get maximum number of waves that can
        # execute on a CU (multi-processor)  in parallel.
        MAX_NUM_THREADS = properties["max_threads_per_sm"]
        max_num_waves = MAX_NUM_THREADS // WARP_SIZE
        occupancy = min(NUM_GPRS // WARP_SIZE // n_regs, max_num_waves) // num_warps
    else:
        occupancy = NUM_REGS // (n_regs * WARP_SIZE * num_warps)
    occupancy = min(occupancy, SIZE_SMEM // size_smem)
    num_programs = NUM_SM * occupancy

    num_programs = min(num_programs, n_rows)

    # Create a number of persistent programs.
    kernel[(num_programs, 1, 1)](y, x, x.stride(0), y.stride(0), n_rows, n_cols, BLOCK_SIZE, num_stages)
    return y
```

### 问题思考

1. num_stages作用是什么？一般怎么设置？

num_stages代表软件流水线的级数。它越大，流水线越长，意味着计算当前stage时，可以将其之前所有stage的数据与预加载至shared memory中。

对于Amper/Hopper架构的GPU，shared memory比较大，num_stages可以设置为4；对于更早的GPU，shared memory较小，num_stages需要设置较小。

2. Block数量计算方式

```python
occupancy = NUM_REGS // (n_regs * WARP_SIZE * num_warps)
``` 

这里的n_regs是一个线程占用的寄存器数量。NUM_REGS为SM的寄存器总数，WARP_SIZE*num_warps为一个block所占用的线程数，occupancy即为block数量。

请注意，block数量不仅受限于寄存器，还受限于shared memory。如果一个block使用的寄存器或者shared memory越大，那么block数量就会越少。


## 计算kernel代码

### 样例代码

```python
@triton.jit
def softmax_kernel(output_ptr, input_ptr, input_row_stride, output_row_stride, n_rows, n_cols, BLOCK_SIZE: tl.constexpr,
                   num_stages: tl.constexpr):
    # starting row of the program
    row_start = tl.program_id(0)
    row_step = tl.num_programs(0)
    for row_idx in tl.range(row_start, n_rows, row_step, num_stages=num_stages):
        # The stride represents how much we need to increase the pointer to advance 1 row
        row_start_ptr = input_ptr + row_idx * input_row_stride
        # The block size is the next power of two greater than n_cols, so we can fit each
        # row in a single block
        col_offsets = tl.arange(0, BLOCK_SIZE)
        input_ptrs = row_start_ptr + col_offsets
        # Load the row into SRAM, using a mask since BLOCK_SIZE may be > than n_cols
        mask = col_offsets < n_cols
        row = tl.load(input_ptrs, mask=mask, other=-float('inf'))
        # Subtract maximum for numerical stability
        row_minus_max = row - tl.max(row, axis=0)
        # Note that exponentiation in Triton is fast but approximate (i.e., think __expf in CUDA)
        numerator = tl.exp(row_minus_max)
        denominator = tl.sum(numerator, axis=0)
        softmax_output = numerator / denominator
        # Write back output to DRAM
        output_row_start_ptr = output_ptr + row_idx * output_row_stride
        output_ptrs = output_row_start_ptr + col_offsets
        tl.store(output_ptrs, softmax_output, mask=mask)
```

### 几个问题

1. block内部的线程是如何分配的？没看到单个线程的索引

从CUDA的线程视角来看，这个确实不太明确。但是Triton的编程模型是SPMD，即single program multiple data。

在Triton你不用担心各个线程怎么索引，你只需将block作为一个整体来处理对应的块数据。

```python
for row_idx in tl.range(row_start, n_rows, row_step, num_stages=num_stages)
```
上述的row_idx代表当前program（即当前block）需要处理的行索引

然后对于每一行，以block线程大小（即num_warps*WARP_SIZE）来处理整行数据，如下

```python
col_offsets = tl.arange(0, BLOCK_SIZE)
input_ptrs = row_start_ptr + col_offsets
# Load the row into SRAM, using a mask since BLOCK_SIZE may be > than n_cols
mask = col_offsets < n_cols
row = tl.load(input_ptrs, mask=mask, other=-float('inf'))
# Subtract maximum for numerical stability
row_minus_max = row - tl.max(row, axis=0)
```
**tl.load**和**tl.max**等都是将数据按照张量形式来处理，在其内部Triton编译器会将其分配给block内的线程。


