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
    # 同时只有一个资源能被访问    
    with lock:
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


# 可重入锁RLock acquire方法能够不被阻塞的被一个线程调用多次
# acquire 和 release 要相同的次数

import threading 

lock = threading.Lock()

print('First try:', lock.acquire())
# print('First try:', lock.release())
print('Second try:', lock.acquire(0))  # 0 不等待

lock = threading.RLock()

# 使用RLock 能重新获得这个锁
print('First try:', lock.acquire())
print('Second try:', lock.acquire(0))


# Condition条件 所有线程接收到后都会处理
# 一个线程等待一个条件 另一个线程发出这个条件
# 生产者 消费者模型

import time
import threading

def consumer(cond):
    t = threading.currentThread()
    with cond:
        cond.wait()  # 等待满足的条件
        print(f'{t.name}: Resource is available to consume')
    
def producer(cond):
    t = threading.currentThread()
    with cond:
        print(f'{t.name}: Making resource available')
        cond.notifyAll()  # 唤醒消费者

condition = threading.Condition()

c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
p = threading.Thread(name='p', target=producer, args=(condition,))

# 先启动消费者 之后启动生产者
c1.start()
time.sleep(1)
c2.start()
time.sleep(1)
p.start()

# Event事件 只有一个线程去处理
import time 
import threading
from random import randint

def consumer(event, l):
    t = threading.currentThread()
    while 1:
        event_is_set = event.wait(2)
        if event_is_set:
            try:
                integer = l.pop()
                print(f'{integer} poped from list by {t.name}')
                event.clear()  # 重置条件状态
            except IndexError: # 为了让刚启动容错
                pass

def producer(event, l):
    t = threading.currentThread()
    while 1:
        integer = randint(10, 100)
        l.append(integer)
        print(f'{integer} append to list by {t.name}')
        event.set()  # 设置条件
        time.sleep(1)

event = threading.Event()

l = []

threads = []

for name in ('consumer1', 'consumer2'):
    t = threading.Thread(name=name, target=consumer, args=(event, l))
    t.start()
    thread.append(t)

p = threading.Thread(name='producer1', target=producer, args=(event, l))
p.start()
threads.append(p)

for t in threads:
    t.join()


# 队列

# 优先级队列

# 线程池



