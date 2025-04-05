---
title: "NVIDIA multi-process service"
subtitle: "usage and internals"
layout: post
author: "Peter Lau"
published: true
header-style: text
tags:
  - Computer science
  - HPC
  - nvidia
categories:
  - HPC
---


## 使用场景




## 架构

![](https://docs.nvidia.com/deploy/mps/_images/image2.png)

对于多个CPU process发起的cuda任务，scheduler会调配时间片分配给每个process；由上图可知，GPU在执行当前process任务一定时间后，会切换执行另一个process的任务，存在许多的context-switch。

![](https://docs.nvidia.com/deploy/mps/_images/image3.png)

MPI(Message Pass Interface)


## 实践


## 参考信息

1. [Multi-Process Service](https://docs.nvidia.com/deploy/mps/index.html)