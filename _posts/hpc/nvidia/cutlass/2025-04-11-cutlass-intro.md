---
title: "cutlass学习之初识"
subtitle: "Intro"
layout: post
author: "Peter Lau"
published: false
header-style: text
tags:
  - Computer science
  - HPC
  - Nvidia
  - cutlass
---


<div>
  <img class="cutlass" src="/img/hpc/cutlass/cutlass关键概念.png" width="500" height="300" alt="cutlass intro">
</div>


## 关键概念

### Tensor



### Layout

$Tensor \in R^{8\times15}$

$Tensor$是可以嵌套的

$HierachyTensor \in R^{(2,4),(3,5)}$

这里的$(2,4)$分别代表tensor内层行数和外层行数；$(3,5)$分别代表tensor内层列数和外层列数

对应的$stride \in R^{(3,6),(1,24)}$


## 参考链接

1. [CUTLASS 2.x与3.x](https://www.bilibili.com/video/BV1XH4y1c7JZ/?spm_id_from=333.1387.search.video_card.click&vd_source=47335eadf4a3037631ddd45e49be7235)