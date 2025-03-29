---
title: "Prefect framework series one"
subtitle: "Python workflow"
layout: post
author: "Peter Lau"
published: true
header-style: text
tags:
  - Computer science
  - Software
  - Python
---


<figure style="text-align: center">
    <img class="prefect logo" src="/img/prefect/prefect_logo.png" width="260" height="200">
    <figcaption style="font-style: italic; color: #666;">prefect logo</figcaption>
</figure>


## 背景

最近经常需要使用python脚本处理数据，在目标场景中数据需要经过多个环节处理才能完成。最初，个人使用多个python脚本，每个脚本对应一个环节，最后再使用shell或者python将这些环节串起来。

后来发现，这些代码可用性较差、不方便维护且需要引入额外的处理比如日志监控和差错重试等。如果去重构也需要再花些时间去梳理，RoI并不高。有无可能从刚开始就按照工作流的形式规范各个环节呢？有的，使用[Prefect](https://docs.prefect.io/v3/get-started/index)！



## Prefect

### flow与task

```python
import datetime
from prefect import flow, task


@task(name="My Example Task", 
      description="An example task for a tutorial.",
      task_run_name="hello-{name}-on-{date:%A}")
def my_task(name, date):
    pass


@flow
def my_flow():
    # creates a run with a name like "hello-marvin-on-Thursday"
    my_task(name="marvin", date=datetime.datetime.now(datetime.timezone.utc))

if __name__ == "__main__":
    my_flow()
```


```python
from prefect import flow

@flow(
    name="My Flow", description="My flow with a name and description", log_prints=True)
def my_flow():
    print("Hello, I'm a flow")


if __name__ == "__main__":
    my_flow()
```


使用@flow和@task来标记**任务流**和**具体任务**,借此可以开发中便捷地标示出主要模块以及主要流程，不需要引入额外的注释做说明。

flow的配置可参考[flow-settings](https://docs.prefect.io/v3/develop/write-flows#flow-settings)

task的配置可参考[task-settings](https://docs.prefect.io/v3/develop/write-tasks)

flow可根据场景需求进行定向设置，例如flow编排，状态管理和重试等；同样地，task也可以设置并发度、超时和重试等。

### flow monitoring

本地可以搭建一个prefect flow运行监控服务，操作流程明细可参考[Prefect](https://docs.prefect.io/v3/manage/server/index)

启动本地端口4200的监控服务

```shell
prefect config set PREFECT_API_URL="http://127.0.0.1:4200/api"

prefect server start
```


运行本地按照prefect flow编写的脚本，流程监控如下


<figure style="text-align: center">
    <img class="prefect dashboard" src="{{ site.baseurl }}/img/prefect/prefect_dashboard_flow_task.png" width="260" height="200">
    <figcaption style="font-style: italic; color: #666;">prefect dashboard</figcaption>
</figure>

prefect dashboard 可以总览最近运行的flow和task


<figure style="text-align: center">
    <img class="prefect runs" src="{{ site.baseurl }}/img/prefect/prefect_runs.png" width="260" height="200">
    <figcaption style="font-style: italic; color: #666;">prefect runs</figcaption>
</figure>

prefect runs可以查询各种运行状态的flow和task


<figure style="text-align: center">
    <img class="flow detail" src="{{ site.baseurl }}/img/prefect/prefect_flow_detail.png" width="260" height="200">
    <figcaption style="font-style: italic; color: #666;">prefect flow detail</figcaption>
</figure>

prefect flow可以查询flow运行时的日志和行为
