#读者-写者模型：
#mutex 保护对 reader_count 的修改。
#write_lock 确保写者独占访问。

import threading
import time
import random

# 信号量和计数器
mutex = threading.Lock()  # 保护 reader_count 的锁
write_lock = threading.Semaphore(1)  # 写者锁。如果大于0则减1，让写者获得访问权限；如果为0，线程将被阻塞直到其他写者释放信号量。
reader_count = 0  # 当前读者数量

def reader(reader_id):
    global reader_count
    while True:
        time.sleep(random.uniform(0.5, 2))  # 模拟读取请求时间

        with mutex:  # 修改 reader_count 的临界区
            reader_count += 1
            if reader_count == 1:  # 第一个读者阻止写者
                write_lock.acquire() 
        print(f"Reader {reader_id} is reading.")
        time.sleep(random.uniform(0.5, 1.5))  # 模拟读操作

        with mutex:  # 修改 reader_count 的临界区
            reader_count -= 1
            if reader_count == 0:  # 最后一个读者释放写者
                write_lock.release()

def writer(writer_id):
    while True:
        time.sleep(random.uniform(1, 3))  # 模拟写入请求时间

        write_lock.acquire()  # 写者需要独占访问
        print(f"Writer {writer_id} is writing.")
        time.sleep(random.uniform(1, 2))  # 模拟写操作
        write_lock.release()  # 释放写者锁

# 创建读者和写者线程
readers = [threading.Thread(target=reader, args=(i,)) for i in range(3)]
writers = [threading.Thread(target=writer, args=(i,)) for i in range(2)]

for r in readers:
    r.start()
for w in writers:
    w.start()

for r in readers:
    r.join()
for w in writers:
    w.join()

