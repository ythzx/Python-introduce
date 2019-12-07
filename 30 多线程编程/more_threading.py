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

# Event事件 只有一个线程去处理 谁接收谁处理
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
    threads.append(t)

p = threading.Thread(name='producer1', target=producer, args=(event, l))
p.start()
threads.append(p)

for t in threads:
    t.join()

"""
86 append to list by producer1
86 poped from list by consumer2
83 append to list by producer1
83 poped from list by consumer2
37 append to list by producer1
37 poped from list by consumer2
22 append to list by producer1
22 poped from list by consumer2
98 append to list by producer1
98 poped from list by consumer1
100 append to list by producer1
100 poped from list by consumer2
42 append to list by producer1
42 poped from list by consumer1
100 append to list by producer1
100 poped from list by consumer1
40 append to list by producer1
40 poped from list by consumer2
58 append to list by producer1
58 poped from list by consumer2
87 append to list by producer1
87 poped from list by consumer2
90 append to list by producer1
90 poped from list by consumer2
"""


# 队列 生产者向队列中添加 消费者从队列中获取
# 1 put 向队列中添加对象
# 2 get 从队列中删除并返回一个对象
# 3 task_done 完成任务时调用
# 4 join 阻塞 直到所有项目被处理

import time
import threading
from random import random 
from queue import Queue

q = Queue()

def double(n):
    return n * 2

def producer():
    while 1:
        wt = random()
        time.sleep(wt)
        q.put((double,wt))

def consumer():
    while 1:
        task, arg = q.get()
        print(f'task: {task}')
        print(f'arg: {arg}')
        print(arg, task(arg))
        q.task_done()

for target in(producer, consumer):
    t = threading.Thread(target=target)
    t.start()

# 优先级队列PriortyQuery
import time 
import threading
from random import randint
from queue import PriorityQueue

q = PriorityQueue()

def double(n):
    return n * 2

def producer():
    count = 0
    while 1:
        if count > 5:
            break
        pri = randint(0, 100)
        print(f'put: {pri}')
        q.put((pri, double, pri)) # 第一项是优先级 数字越小 优先级越高
        count += 1

def consumer():
    while 1:
        if q.empty():
            break
        pri, task, arg = q.get()
        print(f'PRI: {pri} {arg} *2 = {task(arg)}')
        time.sleep(0.1)

t = threading.Thread(target=producer)
t.start()
time.sleep(1)
t = threading.Thread(target=consumer)
t.start()
"""
put: 37
put: 56
put: 39
put: 23
put: 45
put: 40
PRI: 23 23 *2 = 46
PRI: 37 37 *2 = 74
PRI: 39 39 *2 = 78
PRI: 40 40 *2 = 80
PRI: 45 45 *2 = 90
PRI: 56 56 *2 = 112
"""

# 线程池
# 手动实现线程池

import time
import threading
from random import random
from queue import Queue

def doubel(n):
    return n * 2


class Worker(threading.Thread):
    def __init__(self, queue):
        super(Worker, self).__init__()
        self._q = queue
        self.daemon = True
        self.start()
    
    def run(self):
        while 1:
            f, args, kwargs = self._q.get()
            try:
                print(f'USE: {self.name}')
                print(f(*args, **kwargs))
            except Exception as e:
                print(e)
            self._q.task_done()
        

class ThreadPool:
    def __init__(self, num_t=5):
        self._q = Queue(num_t)
        for _ in range(num_t):
            Worker(self._q)
        
    def add_task(self, f, *args, **kwargs):
        self._q.put((f, args, kwargs))
    
    def wait_complete(self):
        self._q.join()

pool = ThreadPool()

for _ in range(8):
    wt = random()
    pool.add_task(double, wt)
    time.sleep(wt)

pool.wait_complete()

"""
USE: Thread-202
0.3289221727443976
USE: Thread-203
1.941427406228165
USE: Thread-204
1.4668008298757944
USE: Thread-205
0.23496561121950066
USE: Thread-206
1.8221948868451534
USE: Thread-202
1.4666381815129967
USE: Thread-203
1.3545860243223637
USE: Thread-204
1.68321523133081
"""
