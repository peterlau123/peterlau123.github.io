---
title: "Environment variables"
subtitle: "在开发中的应用"
layout: post
author: "Peter Lau"
published: false
header-style: text
tags:
  - Programming
---

# Environment variables

环境变量，顾名思义，变量是与运行环境相关的参数。我们在操作系统中经常见到的**PATH**，**LD_LIBRARY_PATH**和**CUDA_VISIBLE_DEVICES**等都是环境变量。

除了系统自带的环境变量，我们自己也可以定义，那么问题来了：什么时候我们需要自己定义一些环境变量呢？

我们知道程序运行中通常包含上下文，英文名字叫**context**，上下文中通常也包含一些变量设置，一般情况下这些设置可以通过程序启动时候加载相应的配置文件来完成。但是有些情况下，这种做法就行不通了。请考虑如下的系统结构：

```mermaid
graph TD;

```



环境变量对程序应用的影响，何时应当设置环境变量

pytorch应用环境变量进行memory alloc相关设置
