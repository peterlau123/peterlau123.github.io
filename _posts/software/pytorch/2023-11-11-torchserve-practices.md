---
title: "torchserve模型服务"
subtitle: "optmization strategies"
layout: post
author: "Peter Lau"
published: true
header-style: text
tags:
  - Computer science
  - Deep Learning
  - Pytorch
---


<div>
  <img class="torchserve" src="/img/torchserve/torchserve.jpg" width="500" height="300" alt="torchserve Architecture">
</div>


## 基本处理单元

<div>
  <img class="torchserve" src="/img/torchserve/torchserve_basic_unit.png" width="500" height="300" alt="torchserve Architecture">
</div>

**Model**对应内部是一个**Handler**，包含*preProcessing*，*inference*和*postProcess*三部分。

**workflow**是一个有向无环图，每个节点代表一个处理任务；上图显示整个流程包含前后处理以及三个模型节点。


```Yaml
models:
    #global model params
    min-workers: 1
    max-workers: 4
    batch-size: 3
    max-batch-delay : 5000
    retry-attempts : 3
    timeout-ms : 5000
    m1:
       url : model1.mar #local or public URI
       min-workers: 1   #override the global params
       max-workers: 2
       batch-size: 4
    m2:
       url : model2.mar
    m3:
       url : model3.mar
       batch-size: 3
    m4:
      url : model4.mar
dag:
  pre_processing : [m1]
  m1 : [m2]
  m2 : [m3]
  m3 : [m4]
  m4 : [postprocessing]
```

在workflow配置中，我们不仅可以设置工作流，还可以设置model节点的worker数量、输入batch-size大小，处理延迟，重试次数等

这里的worker对应一个线程，多个线程会运行多个model实例

Torchserve默认运行在单个JVM进程中，所有的模型加载和处理都在此进程中完成；每个workflow的节点会通过线程池处理并发请求


## 优化策略

### 并发度

这里涉及：

+ 每个模型的worker数量
+ 每个mdoel可以设置的GPU数量

单GPU上，不推荐通过调大worker数量来增加推理吞吐量。因为多线程模型实例，在GPU上会是顺序执行，不会是真正的多模型并行执行。

当然，如果模型前后处理也是耗时的任务，那么通过多workder可以拆分requests，并发执行前后处理，降低单worker的工作负载，提高吞吐。
如下图所示：

![](https://mermaid.ink/img/pako:eNpdkM1ugzAQhF_F2jNBNqb8-NBLe2wllB6QGnKwwhJQAVNjK00R714HgtTWJ8_Ot-P1TnBSJYKAs5ZDTV72RU_c2bODxk-LoxmPZLd7JBk7XJT-qFp1IYPGQasTjuNxpTO2MPnKoCbsnxFsRnA38tXIgl-pajR_Y_PgDoHnxmtKEEZb9KBD3cmbhOkGFmBq7LAA4a4lVtK2poCin13bIPt3pbqtUyt7rjdhh1IafG6k-7ojKtmOriqtUW_X_rRRWDZG6dd1ScuuXAz2JeonZXsDgj3Q5R0QE3yB4Iz7PKVhFEZxwpyKPbiCSCPfleKEp2mYsITPHnwvg1E_jmmcphGPkpAmAeXzD1UGexM?type=png)


多GPU，通过多worker可以将模型实例分布在不同的GPU上，提高吞吐量的同时降低延迟

### Micro-batching


![](https://mermaid.ink/img/pako:eNp1kD9vgzAQxb8KuplE2OavhyztEqmVonRryGDhIyAFmxpbaor47nUgLFXqyXf3e_fsN0KlJQKHixF9E7wdSxX4czwZ_HI42OEcbDa74EBOvcHe6AqHYWMbg0IG5PyAF4Q-QegDOZCZ2Z9aVaNBVeE6oMtgqfbLprubHuw_ditEn0H0D8SeQewMof9wK4Fb4zCEDk0n7iWMd3kJtsEOS-D-KrEW7mpLKNXkZb1Qn1p3q9Jod2nWwvVSWHxthQ_TE7W4Dr4rnNUfN1WtFMrWavO-xD6n79egkmhetFMWOKXp7AN8hG_gLIq3RR6laZGTKI2yOIQbcELibZ7TJC8oo0nGkmwK4Wd-WbTNCEuzghRxnEQsy-PpF-0NlZg?type=png)



## 参考信息

1. [torchserve interns](https://github.com/pytorch/serve/blob/master/docs/internals.md)
2. [torchserve micro-batching](https://github.com/pytorch/serve/blob/master/examples/micro_batching/README.md)