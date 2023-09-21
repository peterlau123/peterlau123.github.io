
# packet
数据结构的设计，不是直接packet<T>的形式，而是HolderBase-->Holder<T>，Holder<T>是packet成员变量的形式

# caculator

caculatorOptions
caculatorGraphConfig

# graph

可以使用C++构建graph
支持cylic graph


# stream

DefaultInputStreamHandler

SyncSetInputStreamHandler

ImmemediateInputStreamHandler


# timestamp

需要各个输入source的timestamp严格保持一致么

flock的输入batch，各路视屏流的frame时间戳不需要严格保持一致

# flow control

max_queue_size

flocw limit caculator
可以控制最多输入多少个packet

# 性能优化考虑因素

number of threads
maximum queues size of input streams


