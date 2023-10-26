---
title: "mediapipe"
subtitle: "数据结构"
layout: post
author: "Peter Lau"
published: true
header-style: text
tags:
  - mediapipe
  - C++
---

# Packet

![](https://cdn.nlark.com/yuque/0/2023/jpeg/32387092/1681093494430-499030fd-814d-4f7d-b8be-cdc46c55f9ec.jpeg)

packet内部持有std::shared_ptr<packet_internal::HolderBase> holder_
packet的创建使用外部的packet_internal::Create来进行，更具体的如下
```cpp
template <typename T,
typename std::enable_if<!std::is_array<T>::value>::type* = nullptr,
typename... Args>
Packet MakePacket(Args&&... args) {  // NOLINT(build/c++11)
    return Adopt(new T(std::forward<Args>(args)...));
}


template <typename T>
Packet Adopt(const T* ptr) {
  CHECK(ptr != nullptr);
  return packet_internal::Create(new packet_internal::Holder<T>(ptr));
}


Packet Create(HolderBase* holder) {
  Packet result;
  result.holder_.reset(holder);
  return result;
}

Packet Create(HolderBase* holder, Timestamp timestamp) {
  Packet result;
  result.holder_.reset(holder);
  result.timestamp_ = timestamp;
  return result;
}

Packet Create(std::shared_ptr<HolderBase> holder, Timestamp timestamp) {
  Packet result;
  result.holder_ = std::move(holder);
  result.timestamp_ = timestamp;
  return result;
}
```
# Caculator


## Caculator node

## Caculator graph

## Caculator runner


