#coding: utf8

from datetime import datetime

def func1():
    print('inside func1')
    return 1

# 这是是将其抽象 但是调用的时候是用do函数而不是func函数 
def do(func):
    rs = func()
    print(datetime.now())
    return rs

# 工厂函数 返回函数wrapper
# 装饰器：返回一个包装后的函数wrapper
def do(func):
    def wrapper():
        rs = func()
        print(datetime.now())
        return rs
    return wrapper

# 在java中装饰器是一种设计模式
# Python中天然支持，@是装饰器的语法糖

@do
def func1():
    print('insode fcun1')
    return 1

## 装饰器应用场景

## do 函数的副作用
def func2():
    """func2 doc"""
    print('inside func2()')
    return 2

func2 = do(func2)
func2.__name__ # __wrapper
func2.__doc__ # 空

## 使用装饰器后保留原函数的属性
from functools import wraps

def do(func):
    @wraps(func)  # 使用wrapers 包装后能保留原函数的属性
    def wrapper():
        rs = func()
        print(datetime.now())
        return rs
    return wrapper


# 给函数的类装饰器

class Common:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print(f'args: {args}')
        return self.func(*args, **kwargs)

@Common
def test(num):
    print(f'Nmuber: {num}')
  
"""
In [40]: test(10)   == Common(test)(10)         
args: (10,)                   
Nmuber: 10                    
                              
In [41]: Common(test)(10)     
args: (10,)                   
args: (10,)                   
Nmuber: 10   
"""    

# 函数装饰器中添加参数
def common(func):
    def wrapper(*args, **kwargs):
        rs = func(*args, **kwargs)
        return rs
    return wrapper


# 给类用的函数装饰器 

import attr 

@attr.s(hash=True)
class Product(object):
    id = attr.ib()
    author_id =  attr.ib()

# borg设计模式
# 解决了同一个类的实例状态一致性的问题
# 相比单例模式能共享资源，状态的同步和共用

def borg(cls):
    cls._state = {}  # 类变量对于不同实例是一样的
    orig_init = cls.__init__
    def new_init(self, *args, **kwargs):
        self.__dict__ = cls._state  # 在装饰器中重新绑定了__dict__, 类变量变成了实例变量
        orig_init(self, *args, *kwargs)
    cls.__init__ = new_init
    return cls

@borg
class A:
    def common(self):
        print(hex(id(self)))

a, b = A(), A()

# 设置a.d 后 b.d 也能访问


# 带参数的装饰器
# 多了一层 用common包装了一层

def common(*args, **kwargs):
    a = args
    def _common(func):
        def _deco(*args, **kwargs):
            print(f'args : {args} {a}')
            return func(*args, **kwargs)
        return _deco
    return _common

@common('abc')
def test(num):
    print(f'Number: {num}')

test(10) == common('abc')(test)(10)
