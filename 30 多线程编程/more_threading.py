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

# 同步机制

# 信号量
# 计数器 锁
import time 
from random import random 
from threading import Thread, Semaphore

sema = Semaphore(3)

def foo(tid):
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

# Lock

# 可重入锁

# 条件
# 生产者 消费者

# Event事件

# 队列

# 优先级队列

# 线程池



