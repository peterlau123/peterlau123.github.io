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