---
title: "Stable diffusion walk through"
subtitle: "From 1.x to 3.x"
layout: chirpy-post
author: "Peter Lau"
published: true
header-style: text
tags:
  - Computer science
  - LLM
  - Stable diffusion
---


<div>
  <img class="shadow" src="/img/stable_diffusion/sd3.5_medium_demo.jpg" width="800" height="250" alt="sd 3.5 medium"
</div>

## 概览


## 模型系列

### 1.x

<div>
  <img class="shadow" src="/img/stable_diffusion/stable_diffusion_arch.png" width="800" height="250" alt="sd arch"
</div>

#### 训练阶段

1. Diffusion process使用VAE编码器，输出潜在空间编码表示
2. 在潜在空间逐步进行噪声添加
3. 将携带噪声的潜在空间表示送入UNet
4. UNet多次迭代，每次迭代输入 控制文本，当前时间向量和上一次的UNet输出
5. 计算原图和去噪输出图损失

#### 推理阶段

1. 输入噪声和控制文本
2. 生成去噪图片

#### 网络结构




### 3.5

### Medium


<div>
  <img class="shadow" src="/img/stable_diffusion/mmdit-x.png" width="800" height="300" alt="sd 3.5 medium"
</div>


## 参考信息




