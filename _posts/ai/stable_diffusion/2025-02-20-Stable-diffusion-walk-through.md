---
title: "Stable diffusion walk through"
subtitle: "From 1.x to 3.x"
layout: post
author: "Peter Lau"
published: false
header-style: text
tags:
  - Computer science
  - LLM
  - Stable diffusion
---


## StableDiffusion总架构

<div>
  <img class="shadow" src="/img/stable_diffusion/stable_diffusion_arch.png" width="800" height="250" alt="sd arch">
</div>

上图中
$x$代表输入原图，$\tilde{x}$代表输出生成图

$\mathcal{E}$代表编码器，$D$代表解码器

### 各个组件
#### Forward Diffusion process

$z$代表潜在空间表示，$z_{T}$代表加噪声后的最终潜在空间表示

加噪声的过程是分次进行的，每次的输入是上次叠加噪声后的潜在空间表示$z_{i}$，输出是潜在空间表示$z_{i+1}$

#### Reverse Diffusion process

类似前向扩散过程，后向也是个逐步迭代的过程，此时

每一轮扩散的输入是上一轮输出记为$z_{T-i}$和条件控制信息，输出是$z_{T-i-1}$，由此反复迭代直至输出$z$

#### 条件控制

T$_\theta$是条件控制网络，可将输入的控制信息如文本、图片和语意分割图等转化为embedding

#### UNet

##### self-attention

对于输入的$x \in R^{C \times H \times W}$，进行先行投影变换得到$Q,K,V$，如下：
$$
Q = W_{Q} \times x , W_{Q} \in R^{d \times CHW}\\
K = W_{K} \times x , W_{K} \in R^{d \times CHW}\\
V = W_{V} \times x, W_{V} \in R^{d \times CHW}
$$

$$
y=softmax(\frac{QK^T}{\sqrt{d}})V
$$

自注意力可以获取图片全局信息之间的关系

##### cross-attention


### 训练阶段

1. Diffusion process使用VAE编码器，输出潜在空间编码表示
2. 在潜在空间逐步进行噪声添加
3. 将携带噪声的潜在空间表示送入UNet
4. UNet多次迭代，每次迭代输入**控制文本、当前时间向量和上一次的UNet输出**
5. 计算原图和去噪输出图损失

### 推理阶段

1. 输入噪声和控制文本
2. 生成去噪图片

## 模型系列
### stable-diffusion-xl
#### 网络结构

<div>
  <img class="shadow" src="/img/stable_diffusion/sd_xl_1_0.png" width="800" height="250" alt="XL pipeline">
</div>

Base模型输入是prompt，输出是潜在空间表示；refiner模型输入是潜在空间表示，输出是生成结果图片

### stable-diffusion-2-1-base

### stable-diffusion-3-medium

### stable-diffusion-3.5-medium

<div>
  <img class="shadow" src="/img/stable_diffusion/sd3.5_medium_demo.jpg" width="800" height="250" alt="sd 3.5 medium">
</div>

<div>
  <img class="shadow" src="/img/stable_diffusion/mmdit-x.png" width="800" height="300" alt="sd 3.5 medium">
</div>


## 参考信息

[Illustrated diffusion](https://jalammar.github.io/illustrated-stable-diffusion/?utm_source=chatgpt.com)

[ApxML](https://apxml.com/courses/advanced-diffusion-architectures/chapter-2-advanced-unet-architectures/unet-attention-mechanisms)




