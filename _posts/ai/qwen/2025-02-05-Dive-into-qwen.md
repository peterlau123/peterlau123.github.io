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

# LLM



# MLLM

## Qwen-VL

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

### 预训练

使用image-text数据集进行预训练，数据集总大小5b的image-text对，经过数据清洗，得到1.4Bimage-text对

输入图片分辨率$224\times224$

QwenLM权重固定，仅学习ViT和Adapter的权重

### 多任务预训练

使用7个任务的数据进行训练，包括Captioning，VQA和OCR等，数据量76.8M，数据格式如下：

<div>
  <img class="shadow" src="/img/qwen/qwen-vl-multitask-data-format.png" width="500" height="300" alt="Qwen-VL Architecture">
</div>


输入图片分辨率$448\times448$

QwenLM、ViT和Adapter都用来学习

### 微调

为增强指令遵循和对话能力，使用指令微调数据，数据量350K，
数据格式如下：

<div>
  <img class="shadow" src="/img/qwen/qwen-vl-sft-format.png" width="500" height="300" alt="Qwen-VL Architecture">
</div>

QwenLM和Adapter用来学习，ViT权重固定

### 小结

可以看到，对于Qwen-VL模型，为了引入视觉多模态信息，整个模型是分开训练的。首先训练image-caption能力，再拓展至多任务的图文能力，最后再微调对话能力，所需要的数据量从大到小。

相较于前两阶段的训练，最后一个阶段的训练数据来自LLM自生成，再经过人工清洗构建。

## Qwen2-VL

<div>
  <img class="shadow" src="/img/qwen/Qwen2-VL-arch.png" width="500" height="300" alt="Qwen2-VL Architecture">
</div>

Qwen2-VL沿用了Qwen-VL的模型架构，但只保留了两个部分：

+ Pretrained LLM
  基于Qwen2模型
+ Visual Encoder
  675M参数的ViT

其中ViT做了更新，可以处理图片和视频以及更多的输入尺度，LLM部分选择更强大的Qwen2。

### 引入特性

#### 动态分辨率

#### 多模态RoPE

#### 统一图片和视频理解

### 训练

同Qwen-Vl一样，Qwen2-VL也分为三个阶段进行训练：

#### 第一阶段

目标：训练对visual-text的理解能力

数据：数据量600B

方法：只训练ViT

#### 第二阶段

目标：训练更细致捕捉visual-text关系的能力

数据：数据量800B（与第一阶段数据不重合），包含多任务数据

方法：训练ViT和LLM


#### 第三阶段

目标：理解和执行跨模态的指令

数据：ChatML格式指令数据

数据格式如下：

<div>
  <img class="shadow" src="/img/qwen/Qwen2-vl-chatml.png" width="500" height="300" alt="Qwen2-VL Architecture">
</div>


方法：固定ViT，微调LLM

### 小结

## Qwen2.5-VL


<div>
  <img class="shadow" src="/img/qwen/Qwen2.5-VL-arch.png" width="500" height="300" alt="Qwen2.5-VL Architecture">
</div>

## Qwen2.5-omni

<div>
  <img class="shadow" src="/img/qwen/Qwen2.5-Omni.png" width="500" height="300" alt="Qwen2.5-Omni Architecture">
</div>