# coding: utf8

# 迭代器Iterator
class Fib:
    """
    斐波那契
    """
    def __init__(self, max):
        self.a = 0
        self.b = 1
        self.max = max
        
    def __iter__(self):
        return self  # 返回对象本身
    
    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration  # 最后一个元素抛出异常
        self.a, self.b = self.b, self.a + self.b 
        return fib

# 生成器Generator
## 生成器是使用普通函数语法定义的迭代器。
## 和普通函数的区别是使用yield 而不是使用return返回值
# yield 会挂起函数 
# 生成器的本质也是迭代器

def my_gen():
    yield 1
    yield 2

# 生成器表达式

g = (i for i in range(10) if i % 2)



# 协程 Coroutine
# yield 在右侧
# send 把值传递给yield
# 协程 协作
# 在同一个线程中 不需要加锁

def coroutine():
    print("Start")
    x = yield
    print(f'Received: {x}')

def coroutine2(a):
    print("Start: {a}")
    b = yield a 
    print(f'Received: b= {b}')
    c = yield a + b
    print(f'Received: c={c}')

"""
In [49]: coro = coroutine2(1)

In [50]: next(coro)
Start: {a}
Out[50]: 1

In [51]: coro.send(2)
Received: b= 2
Out[51]: 3   # 协程的返回结果是表达式右侧的值

In [52]: coro.send(10)
Received: c=10
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-52-7a1f101c1ec1> in <module>
----> 1 coro.send(10)

StopIteration:
"""

# 回调例子 异步
def framework(logic, callback):
    s = logic()
    print(f'[FX] logic: {s}')
    print(f'[FX] do something....')
    callback(f'async : {s}')


def logic():
    return 'Logic'

def callback(s):
    print(s)

framework(logic, callback)

# 协程实现回调
def framework1(logic):
    try:
        it = logic1()
        s = next(it)
        print(f'FX logic": {s}')
        print(f'FX do something')
        it.send(f'async: {s}')
    except StopIteration:
        pass

def logic1():
    s = 'Logic'
    r = yield s  # 在这里实现异步
    print(r)

"""
In [57]: framework1(logic1)
FX logic": Logic
FX do something
async: Logics
"""

# 生产者 消费者

def consumer():
    """
    消费者是协程
    """
    while True:
        v = yield
        print(f'consume: {v}')

def producer(c):
    for i in range(10, 13):
        c.send(i)

c = consumer()
c.send(None) # == next() 激活协程
producer(c) # 消费者

# 生产者 消费者切换

def consumer():
    r = ''
    while True:
        v = yield r
        print(f'consumer: {v}')
        r = f'Resule: {v*2}'

def producer(c):
    for i in range(10, 13):
        print(f'Produceing... {i}')
        r = c.send(i)
        print(f'consumer return: {r}')

c = consumer()
c.send(None)
producer(c)

"""
Produceing... 10
consumer: 10
consumer return: Resule: 20
Produceing... 11
consumer: 11
consumer return: Resule: 22
Produceing... 12
consumer: 12
consumer return: Resule: 24
"""
