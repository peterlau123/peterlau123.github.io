---
title: "ONNXRuntime API"
subtitle: "APi设计方法"
layout: chirpy-post
author: "Peter Lau"
published: true
header-style: text
tags:
  - Computer science
  - Deep Learning
---

近期的工作由于经常涉及到基于onnxruntime进行模型部署，本着学啥熟悉啥的习惯，上来第一件事就是浏览了它的API。onnxruntime API带给我最大的感觉是清晰，让开发者很难会去误用它的接口。

*include/onnxruntime/core/session/onnxruntime_c_api.h*开头的一段代码就展示了为API的输入和输出等制定的宏。

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


进一步，我们观察一个主要API，**Run**
```c++
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

可以看到，输入与输出被很明显的标记出来。不仅如此，对于数组，可以很清晰地看到它的大小约束；对于参数的读/写属性，也可以很方便通过**_In_reads_**和**_Inout_updates_all_**确认。

好的API就应该这样书写！

