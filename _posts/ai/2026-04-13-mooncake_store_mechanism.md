---
title: "Mooncake Store"
subtitle: "存储机制剖析"
layout: chirpy-post
author: "Peter Lau"
published: true
header-style: text
categories:
  - AI
tags:
  - AI
  - Engineering
---

## Mooncake Store

**本次分析基于Mooncake版本v0.3.9**

### 整体架构设计

<div>
  <img class="shadow" src="/img/mooncake/mooncake-store-preview.png" width="600" height="240" alt="Mooncake Store Architecture">
</div>


## P2P Store

p2p store主要用于大模型checkpoint分发，基于Transfer Engine构建。

试想如果所有GPU卡都从固定的源头同时加载权重切片，那么源头处的带宽会瞬间饱和，无法进一步提升传输性能。

这个方案的独特之处是每个GPU卡在加载完权重切片后，会将其传输到也需要这份切片的GPU卡上，这样源头处的带宽压力就会降低，数据传输效率得到提升。
