# coding:utf8

import threading

def worker():
    print("Work")

thread = []
for i in range(5):
    t = threading.Thread(target=worker)
    thread.append(t)
    t.start()

## 支持输入参数
def worker(num):
    print(f"Work: {num}")

thread = []

for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    thread.append(t)
    t.start()

# 守护和非守护线程

import threading
import time

def daemon():
    print("Daemon Startin")
    time.sleep(3.2)
    print("Daemon Exiting")

def non_daemon():
    print("NonDaemon Srarting")
    print("NonDaemon Exiting")

d = threading.Thread(name='daemon', target=daemon, daemon=True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()
# 主线程等待守护线程
d.join()
t.join()

# 多线程编程中多个线程会同时访问同一资源的
# 同步机制

# 信号量
# 计数器 锁
import time 
from random import random 
from threading import Thread, Semaphore

sema = Semaphore(3)  # 限制同时访问的数量

def foo(tid):
    """
    acquire 计数器-1
    release 计数器+1
    """
    with sema:
        print(f'{tid} acquire sema')
        wt = random() * 2
        time.sleep(wt)
    print(f'{tid} release sema')

threads = []
for i in range(5):
    t = Thread(target=foo, args=(i,))
    t.start()

for t in threads:
    t.join()

"""
# 保证同时只有3个被访问
0 acquire sema
1 acquire sema
2 acquire sema

1 release sema
3 acquire sema
2 release sema
4 acquire sema
3 release sema
4 release sema
0 release sema
"""

# Lock(互斥锁) == 信号量为1 同时只有一个资源访问
# 加锁会牺牲一定的性能
import time
from threading import Thread

value = 0

def get_lock():
    """
    不加锁
    """
    global value
    new = value + 1
    time.sleep(0.001) # sleep 让线程有机会切换
    value = new

threads = []

for i in range(100):
    t = Thread(target=get_lock)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(value) # 结果并不是100 有执行慢的线程最后把结果重写了



import time
from threading import Thread, Lock

value = 0
lock = Lock()

def get_lock():
    """
    加锁
    """
    global value
    with lock:
        """"
        同时只有一个资源能被访问
        """"
        new = value + 1
        time.sleep(0.001) # sleep 让线程有机会切换
        value = new

threads = []

for i in range(100):
    t = Thread(target=get_lock)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(value)


# 可重入锁

# 条件
# 生产者 消费者

# Event事件

# 队列

# 优先级队列

# 线程池



