---
title: "mediapipe"
subtitle: "其他"
layout: post
author: "Peter Lau"
published: false
header-style: text
tags:
  - mediapipe
  - C++
---


# 线程
## Thread safety annotations 
代码中大量使用了thread safety annotations，为了方便在编译期就检查mutex的使用正确性

```cpp
 // Used internally by RunNextTask. Invokes ProcessNode or CloseNode, followed
  // by EndScheduling.
  void RunCalculatorNode(CalculatorNode* node, CalculatorContext* cc)
      ABSL_LOCKS_EXCLUDED(mutex_);

  // Used internally by RunNextTask. Invokes OpenNode, followed by
  // CheckIfBecameReady.
  void OpenCalculatorNode(CalculatorNode* node) ABSL_LOCKS_EXCLUDED(mutex_);

  // Checks whether the queue has no queued nodes or pending tasks.
  bool IsIdle() ABSL_EXCLUSIVE_LOCKS_REQUIRED(mutex_);

  Executor* executor_ = nullptr;

  IdleCallback idle_callback_;

  // The net number of times SetRunning(true) has been called.
  // SetRunning(true) increments running_count_ and SetRunning(false)
  // decrements it. The queue is running if running_count_ > 0. A running
  // queue will submit tasks to the executor.
  // Invariant: running_count_ <= 1.
  int running_count_ ABSL_GUARDED_BY(mutex_) = 0;

  // Number of tasks added to the Executor and not yet complete.
  int num_pending_tasks_ ABSL_GUARDED_BY(mutex_);

  // Number of tasks that need to be added to the Executor.
  int num_tasks_to_add_ ABSL_GUARDED_BY(mutex_);

  // Queue of nodes that need to be run.
  std::priority_queue<Item> queue_ ABSL_GUARDED_BY(mutex_);

  SchedulerShared* const shared_;

  absl::Mutex mutex_;
```

具体解释如下
```cpp
ABSL_GUARDED_BY(mutex_)//代表变量被锁mutex_保护

ABSL_EXCLUSIVE_LOCKS_REQUIRED//代表本线程内调用该函数的时候，已经占有mutex_

ABSL_LOCKS_EXCLUDED//代表本线程内调用该函数的时候，没有占有mutex_
```

当然这样的宏，需要编译器的支持，目前clang是支持静态检查的，也就是所谓的thread safey annotations


参考 
[Thread Safety Analysis — Clang 17.0.0git documentation](https://clang.llvm.org/docs/ThreadSafetyAnalysis.html)

