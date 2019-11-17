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


