---
title: "simdJson"
subtitle: "Code Walkthrough"
layout: post
author: "Peter Lau"
published: true
header-style: text
tags:
  - Framework
  - Serialization/Deserialization
  - C++
---

# simdJson

## Motivation



## Features

### Fast

### Less memory consumption



## Mechanism

But how to do to support the folliwing features?

## Lessons

### Systematic error handling

In its code, I usually see the struct

```c++
simdjson::simdjson_result< T >
```

This struct put value and error together,it is useful when we donnot want to take extra action when return result while exception occurs.

As usual,we would like to return default result or fill it with values indicating failure.Instead, done in the above way,we can just check the error inside the above struct.

Very convenient and make code more concise.

```c+++
simdjson_inline error_code  error () const noexcept

simdjson_inline T &     value () &noexcept(false)
```



References

1. Rust option

2. [C++ and Beyond 2012: Andrei Alexandrescu - Systematic Error Handling in C++](https://www.youtube.com/watch?v=kaI4R0Ng4E8)

3. [What's the equivalent of Option and Result in C++?](https://www.reddit.com/r/rust/comments/2f5twr/whats_the_equivalent_of_option_and_result_in_c/?rdt=48674&onetap_auto=true)
