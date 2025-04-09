---
title: "The transformer's optimizations part one"
subtitle: "Paged Attention"
layout: post
author: "Peter Lau"
published: false
header-style: text
tags:
  - Computer science
  - LLM
  - Transformers
  - vLLM 
---


<div>
  <img class="vLLM" src="/img/vllm/vLLM_system_overview.png" width="500" height="300" alt="vLLM system">
</div>

## 背景

### 自回归transformer模型




首先来看自回归transformer模型结构，它主要包含以下部分：
+ input
+ embedding
+ positional encoding
+ Masked MultiHead Attention
+ FeedForward
+ Linear&Softmax
  
  其中**MultiHead Attention**和**FeedFoward**作为一个基础模块可以不断堆叠。


### kv cache matters

<div>
  <img class="vLLM" src="/img/vllm/kv_cache_现状.png" width="500" height="300" alt="current kv cache">
</div>

## Paged Attention机制解析


<div>
  <img class="vLLM" src="/img/vllm/block_table_translation.png" width="500" height="300" alt="block table">
</div>


<div>
  <img class="vLLM" src="/img/vllm/kv_cache_two_requests.png" width="500" height="300" alt="kv_cache two requests">
</div>

### 不同decoding策略



## 参考信息

1. [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)