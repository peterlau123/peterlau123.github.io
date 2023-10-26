---
title: "flatbuffers"
subtitle: "Code Walkthrough"
layout: post
author: "Peter Lau"
published: false
header-style: text
tags:
  - Framework
  - Serialization/Deserialization
  - C++
---

# flatbuffers

## Motivation

>Back in the good old days, performance was all about instructions and cycles. Nowadays, processing units have run so far ahead of the memory subsystem, that making an efficient application should start and finish with thinking about memory. How much you use of it. How you lay it out and access it. How you allocate it. When you copy it.

>Serialization is a pervasive activity in a lot programs, and a common source of memory inefficiency, with lots of temporary data structures needed to parse and represent data, and inefficient allocation patterns and locality.

>If it would be possible to do serialization with no temporary objects, no additional allocation, no copying, and good locality, this could be of great value. The reason serialization systems usually don't manage this is because it goes counter to forwards/backwards compatability, and platform specifics like endianness and alignment.

>FlatBuffers is what you get if you try anyway.

>In particular, FlatBuffers focus is on mobile hardware (where memory size and memory bandwidth is even more constrained than on desktop hardware), and applications that have the highest performance needs: games.


This is a brief motivation extracted from [flatbuffers white paper](https://flatbuffers.dev/flatbuffers_white_paper.html).

After reading this short summary about motivation, I'm really impressed by the author's insights.

On one hand,the passage above does a good example in software engieering about how to do things,that is why do it and why do it so, this is really important in our career.On the other hand,it tells us that flatbuffers mainly foucus on memory efficiency.

I agree on the idea that one should start and finish a program with thinking about memory all the time.Memory issues cannot be ignored in current programming,whether you develop for mobile or serve to support high concurrency.

## Features





## Mechanism

But how to do to support the features above?


