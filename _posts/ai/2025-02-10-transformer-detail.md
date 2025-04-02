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

假设目前输入为 $N$ 个token，经过embedding后，变为 $N \times d$ 矩阵，记为 $I$。($d=512$，下面的 $d_{model}$ 也是同样大小)
那么 $Q,K,V$ 可以通过如下计算得到：

$$
Q = I \times W^Q
$$

$$
K = I \times W^K
$$

$$
V = I \times W^V
$$

其中 $W^Q,W^K,W^V$ 分别为 $d \times d_k, d \times d_k, d \times d_v$ 大小的矩阵，$Q,K,V$ 大小为 $N \times d_k, N \times d_k$ 和 $N \times d_v$。

### single head attention

在上一步的基础上，我们继续：

$$
Attention(Q,K,V)=softmax(\frac{QK^T}{\sqrt{d_k}})V
$$

$QK^T$得到$N*N$的矩阵，再按行执行$softmax$

最终的输出$N*d_v$大小的矩阵

### multi-head attention


$$
\text{MultiHead}(Q,K,V)=\text{Concat}(\text{head}_1,\text{head}_2,\ldots,\text{head}_h)W^O \newline
\text{head}_i=\text{Attention}(QW^Q_i,KW^K_i,VW^V_i)
$$

$$
W^Q_i \in \mathbb{R}^{d_{\text{model}} \times d_k}
$$

$$
W^K_i \in \mathbb{R}^{d_{\text{model}} \times d_k}
$$

$$
W^V_i \in \mathbb{R}^{d_{\text{model}} \times d_v}
$$

$$
W^O \in \mathbb{R}^{h \cdot d_v \times d_{\text{model}}}
$$


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