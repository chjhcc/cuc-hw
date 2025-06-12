#生产者-消费者模型：
#full 信号量控制缓冲区的数据数量。
#mutex 保护对共享缓冲区的访问。

import threading  # 导入线程模块
import time # 导入时间模块
import random # 导入随机模块

BUFFER_SIZE = 5 # 缓冲区大小
buffer = []  # 缓冲区

# 信号量
empty = threading.Semaphore(BUFFER_SIZE)  # 空位信号量
full = threading.Semaphore(0)  # 数据信号量
mutex = threading.Lock()  # 互斥锁

def producer(producer_id):
    while True:
        time.sleep(random.uniform(0.5, 2))  # 模拟生产耗时
        item = random.randint(1, 100)  # 生产的物品

        empty.acquire()  # 等待空位
        with mutex:  # 进入临界区
            buffer.append(item)  # 放入缓冲区
            print(f"Producer {producer_id} has produced: {item}")
        full.release()  # 增加数据信号量

def consumer(consumer_id):
    while True:
        time.sleep(random.uniform(0.5, 3))  # 模拟消费耗时

        full.acquire()  # 等待数据
        with mutex:  # 进入临界区
            item = buffer.pop(0)  # 取出缓冲区的物品
            print(f"Consumer {consumer_id} hasconsumed: {item}")
        empty.release()  # 增加空位信号量

# 创建生产者和消费者线程
producers = [threading.Thread(target=producer, args=(i,)) for i in range(2)]
consumers = [threading.Thread(target=consumer, args=(i,)) for i in range(3)]

for p in producers:
    p.start()
for c in consumers:
    c.start()

for p in producers:
    p.join()
for c in consumers:
    c.join()

