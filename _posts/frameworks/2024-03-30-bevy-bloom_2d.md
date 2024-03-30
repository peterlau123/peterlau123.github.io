---
title: "Bevy"
subtitle: "bloom_s2"
layout: post
author: "Peter Lau"
published: false
header-style: text
tags:
  - Game Engine
  - Computer Graphics
---

# bloom_2d


代码位于*bevy/examples/ad/bloom_2d.rs*


这个游戏主要包含两个系统：**setup**和**update_bloom_settings**。




**setup**生成了5个实体，分别是：


**update_bloom_settings**负责对如下参数进行更新


![bloom_2d_app](./bevy_images/snapshot_of_bevy.png)


问题：

参数怎么传递到实体的？

实体怎么依据不同的参数来更新的？