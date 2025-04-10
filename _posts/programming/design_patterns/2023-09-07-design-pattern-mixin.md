---
title: "Design Pattern"
subtitle: "Mixin"
layout: post
author: "Peter Lau"
published: true
header-style: text
tags:
  - Computer science
  - Design Patterns
---

# Mixin pattern

## Scenario



## Examples


```c++

struct BaseImpl{
    std::shared_ptr<ModuleA> module_a;
    std::shared_ptr<ModuleB> module_b;
    std::shared_ptr<ModuleC> module_c;
};

```

If we implement function F1 and F2,we have to add another module pointers,what should we do?

Suppose we add ModuleD and ModuleE for F1,add ModuleF for F2

The naive solution will be as shown below

```c++
struct F1Impl:public BaseImpl{
    std::shared_ptr<ModuleD> module_d;
    std::shared_ptr<ModuleE> module_e;
};

struct F1Impl:public BaseImpl{
    std::shared_ptr<ModuleF> module_f;
};

```

It is fine for usual common cases,however ,it does not obey  the principle of inheritence.For inheritance, it is mainly related to behavior of class not its data members.

Let's take it in another way,look at the code below.

```c++

template <typename.. Mixins>struct BaseImpl: public Mixins ..{
    std::shared_ptr<ModuleA> module_a;
    std::shared_ptr<ModuleB> module_b;
    std::shared_ptr<ModuleC> module_c;
};

struct F1Impl{
    std::shared_ptr<ModuleD> module_d;
    std::shared_ptr<ModuleE> module_e;
};

struct F1Impl{
    std::shared_ptr<ModuleF> module_f;
};

```

Then if we want to combine *BaseImpl* into F1Impl,that is easy , just write 

```c++
BaseImpl<F1Impl> f1_impl;
```

As you can see, implement this way, we keep the F1Impl and BaseImpl independant from each other.


