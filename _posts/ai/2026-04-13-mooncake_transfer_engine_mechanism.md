---
title: "Mooncake Transfer Engine"
subtitle: "传输机制剖析"
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

## Mooncake transfer engine

**本次分析基于Mooncake版本v0.3.9**

### Transfer engine

<div>
  <img class="shadow" src="/img/mooncake/transfer_engine_arch.png" width="600" height="240" alt="Transfer engine Architecture">
</div>

上图中，**vRAM**代表GPU显存，**DRAM**代表CPU主存，**NVMe**（配合NvMEof协议）属于外接硬盘。


### 相关问题

1. Prefill transfer failed for request rank xxx
