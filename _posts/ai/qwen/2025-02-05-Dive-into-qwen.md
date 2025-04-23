---
title: "Dive into qwen models"
subtitle: "Internals"
layout: post
author: "Peter Lau"
published: false
header-style: text
tags:
  - Computer science
  - LLM
  - Qwen
---




本文对Qwen系列模型的演变进行分析。

## LLM



## MLLM

### Qwen-VL

<div>
  <img class="shadow" src="/img/qwen/Qwen-VL-arch.png" width="500" height="300" alt="Qwen-VL Architecture">
</div>

Qwen-VL的模型架构包含三部分：
+ Pretrained LLM
  基于Qwen-7B模型
+ Visual Encoder
  使用ViT，初始化权重来自Openclip's ViT-bigG
+ Position-aware Vision-Language Adapter

它的训练包含三个阶段：

#### 预训练


#### 多任务预训练

#### 微调

### Qwen2-VL


<div>
  <img class="shadow" src="/img/qwen/Qwen2-VL-arch.png" width="500" height="300" alt="Qwen2-VL Architecture">
</div>


### Qwen2.5-VL


<div>
  <img class="shadow" src="/img/qwen/Qwen2.5-VL-arch.png" width="500" height="300" alt="Qwen2.5-VL Architecture">
</div>

### Qwen2.5-omni

<div>
  <img class="shadow" src="/img/qwen/Qwen2.5-Omni.png" width="500" height="300" alt="Qwen2.5-Omni Architecture">
</div>