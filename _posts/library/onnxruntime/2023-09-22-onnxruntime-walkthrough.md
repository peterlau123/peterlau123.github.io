---
title: "ONNXRuntime"
subtitle: "Code Walkthrough"
layout: post
author: "Peter Lau"
published: true
header-style: text
tags:
  - Framework
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

### API

Good APIs

The APISs  use macros to indicate the input,output,return and also some possible notes when using


```c++
#define _Out_
#define _Outptr_
#define _Out_opt_
#define _Inout_
#define _Inout_opt_
#define _Frees_ptr_opt_
#define _Ret_maybenull_
#define _Ret_notnull_
#define _Check_return_
#define _Outptr_result_maybenull_
#define _In_reads_(X)
#define _Inout_updates_all_(X)
#define _Out_writes_bytes_all_(X)
#define _Out_writes_all_(X)
#define _Success_(X)
#define _Outptr_result_buffer_maybenull_(X)
#define ORT_ALL_ARGS_NONNULL __attribute__((nonnull))
```


```c++
ORT_API2_STATUS(CreateEnv, OrtLoggingLevel log_severity_level, _In_ const char* logid, _Outptr_ OrtEnv** out);

/** \brief Run the model in an ::OrtSession
 *
 * Will not return until the model run has completed. Multiple threads might be used to run the model based on
 * the options in the ::OrtSession and settings used when creating the ::OrtEnv
 *
 * \param[in] session
 * \param[in] run_options If nullptr, will use a default ::OrtRunOptions
 * \param[in] input_names Array of null terminated UTF8 encoded strings of the input names
 * \param[in] inputs Array of ::OrtValue%s of the input values
 * \param[in] input_len Number of elements in the input_names and inputs arrays
 * \param[in] output_names Array of null terminated UTF8 encoded strings of the output names
 * \param[in] output_names_len Number of elements in the output_names and outputs array
 * \param[out] outputs Array of ::OrtValue%s that the outputs are stored in. This can also be
 *     an array of nullptr values, in this case ::OrtValue objects will be allocated and pointers
 *     to them will be set into the `outputs` array.
 *
 * \snippet{doc} snippets.dox OrtStatus Return Value
 */
ORT_API2_STATUS(Run, _Inout_ OrtSession* session, _In_opt_ const OrtRunOptions* run_options,
               _In_reads_(input_len) const char* const* input_names,
               _In_reads_(input_len) const OrtValue* const* inputs, size_t input_len,
               _In_reads_(output_names_len) const char* const* output_names, size_t output_names_len,
               _Inout_updates_all_(output_names_len) OrtValue** outputs);
```

### minimal build

I often see minimal build in TensorRT and onnxruntime

for example

onnxruntime has ORT model format to support memory constrained scenarios

But what is being cut off?
