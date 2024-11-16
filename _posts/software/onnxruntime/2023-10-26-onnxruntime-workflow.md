---
title: "workflow"
subtitle: "ONNXRuntime"
layout: post
author: "Peter Lau"
published: false
header-style: text
tags:
  - Computer science
  - Deep Learning
---

# Code walkthrough

## Classes and config

### Classes

### Config

## Mechanisms


## workflows


### Whole workflow

```
graph TD;

A[Create Environment] --> B[Create inference session]

B --> C[Run the session]

```

### Environment  creation

1. Init ortEnv

2. set inter/intra op thread pool

3. set shared_allocators

4. set logging manager

### Session Initialize

1. set allocator

2. transform graph

    + do graph partitioning

### Session Run

1. provider run/start

2. execute graph


## Lessons

### minimal build

I often see minimal build in TensorRT and onnxruntime

for example

onnxruntime has ORT model format to support memory constrained scenarios

But what is being cut off?
