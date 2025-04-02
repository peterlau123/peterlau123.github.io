---
title: "The transformer's details"
subtitle: "From math to code"
layout: post
author: "Peter Lau"
published: true
header-style: text
tags:
  - Computer science
  - LLM 
---


<div>
  <img class="shadow" src="/img/transformers/transformer_architecture.png" width="500" height="300" alt="Transformer Architecture">
</div>



## 数学表达

### Q,K,V

假设目前输入为$$N$个token，经过embedding后，变为$N*d$矩阵，记为$I$。($d=512$，下面的$d_{model}$也是同样大小)
那么$Q,K,V$可以通过如下计算得到：

$$
\begin{aligned}
Q=I*W^Q
\end{aligned}
$$

$$
\begin{aligned}
K=I*W^K
\end{aligned}
$$

$$
\begin{aligned}
V=I*W^V
\end{aligned}
$$

其中$W^Q,W^K,W^V$分别为$d*d_{k},{d*d_k},{d*d_v}$大小的矩阵，$Q,K,V$大小为$N*d_k,{N*d_k}$和$N*d_v$。

### single head attention

在上一步的基础上，我们继续：

$$
\begin{aligned}
Attention(Q,K,V)=softmax(\frac{QK^T}{\sqrt{d_k}})V
\end{aligned}
$$

$QK^T$得到$N*N$的矩阵，再按行执行$softmax$

最终的输出$N*d_v$大小的矩阵

### multi-head attention

$$
\begin{aligned}
MultiHead(Q,K,V)=Concat(head_1,head_2,...,head_h)W^O\newline
head_i=Attention(QW^Q_i,KW^K_i,VW^V_i)
\end{aligned}
$$

$W^Q_i \in R^{d_{model}*d_k}$

$W^K_i \in R^{d_{model}*d_k}$

$W^V_i \in R^{d_{model}*d_v}$

$W^O \in R^{hd_v*d_{model}}$

从$W^O$的维度可以看出，$Concat$是在$head_i$行方向上进行

Attention论文中$h=8$，$d_{model}=512$，$d_v=d_k=\frac{d_{model}}{h}=64$

### Add&Norm

**Multi-Head Attention**的输出为$N*d_{model}$大小的矩阵

以$N=3,d_{model}=512$为例

多头注意力模块的输出矩阵大小为3*512，输入$x \in R^{3*512}$





## 代码实现


## 参考信息

1. https://jalammar.github.io/illustrated-transformer/
  
2. The Annotated Transformer