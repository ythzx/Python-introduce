# coding: utf8

# 条目基类


class Subject:
    kind = None

    def __init__(self, id, category_id, title):
        self.id = id
        self.category_id = category_id
        self.title = title

    def show_title(self):
        return self.title

    def update_title(self, title):
        self.title = title


# 类的实例化
subject = Subject(1, 1000, '条目1')

# 获取对象的属性
print(subject.kind, subject.id, subject.category_id, subject.title)

# 调用对象的方法
res = subject.show_title()
print(res)

# 方法会更新对象属性
subject.update_title('new title')
res1 = subject.show_title()
res2 = subject.title
# print(res1, res2)

# 覆盖
class Movie(Subject):
    kind = 'movie'

    def __init__(self, id, category_id, title, directors=[]):
        super.__init__(id, category_id, title)
        self.directors = directors

    def show_directors(self):
        return self.directors

    def show_title(self):
        return f'Movie: {self.title}'  # 多态

# MRO 方法解析顺序 Methord Resolution Order

class A:
    def run(self):
        print("A.run")
    
class B(A):
    pass

class C(A):
    def run(self):
        print("C.run")

class D(B,C):
    pass

# 菱形继承 
#   A
#  / \
# /   \
# B   C
# \   /
#  \ /
#   D

# 经典类继承顺序 DBAC

import inspect

inspect.getmro(D)
# Out[3]:
# (<class __main__.D at 0x00000000041DABE8>,
#  <class __main__.B at 0x0000000004037B88>,
#  <class __main__.A at 0x000000000414CB28>,
#  <class __main__.C at 0x0000000004037A68>)


# 新式类继承顺序 DBCA

inspect.getmro(D)
# Out[6]: (__main__.D, __main__.B, __main__.C, __main__.A, object)

# 深度优先会查找到基类，基类中的方法通常是占位用的

# property

class Movies(Subject):
    kind = 'movie'

    def __init__(self, id, category_id, title, directors = []):
        super().__init__(id, category_id, title)
        self._directors = directors

    @property
    def directors(self):
        return self._directors

# 设置setter delter

class Movies1(Subject):
    kind = 'movie'

    def __init__(self, id, category_id, title, directors = []):
        super().__init__(id, category_id, title)
        self._directors = directors

    @property
    def directors(self):
        return self._directors

    @directors.setter   # 给directors 添加setter方法
    def directors(self, value):
        if not isinstance(value, list):
            raise ValueError('invalid value')
        self._directors = value
    
    @directors.deleter
    def directors(self):
        self._directors = []


# 其他方式实现
class Movies2(Subject):
    kind = 'movie'

    def __init__(self, id, category_id, title, directors = []):
        super().__init__(id, category_id, title)
        self._directors = directors

    def get_directors(self):
        return self._directors
    
    def set_directors(self, value):
        if not isinstance(value, list):
            raise ValueError('invalid type')
        self._directors = value

    def del_directors(self):
        self._directors = []
    
    # 不设置具体的set/del方法 使用None占位
    directors = property(get_directors, set_directors, del_directors)


# 静态方法/类方法

class A(object):
    count = 0

    def incr_count(self):
        self.count += 1
    
    @classmethod
    def incr_count2(cls):
        cls.count += 1
     
    @staticmethod
    def incr_count3():
        A.count += 1  # 访问了类的变量，不建议使用
    
    @staticmethod
    def avg(*items): 
        return sum(items) / len(items)

# 静态方法和类方法都访问不到对象变量，因为没有self

# 私有变量
class Employee:
    _kind = 'employee'

    def __init__(self, name):
        self.__name = name

#  e._Employee__name

# 构造方法
# 构造方法主要在创建对象时初始化对象
# __new__ cls
# __init__

class ExampleClass:
    def __new__(cls, *args, **kwargs):
        print("Creating new instance")
        instance = super().__new__(cls)
        instance.PAYLOAD = (args, kwargs)
        return instance
    
    def __init__(self, payload):
        print("Initing instance")
        self.payload =   payload

# 小节:
# __new__ 是类方法 __init__是实例方法
# __new__ 先执行


# 控制属性访问(拦截)
# __getattr__
# __setattr__
# __delattr__
# __getattribute__

class User:
    ...  # ==pass in python3

class Proxy:
    title = "Proxy"
    _data = User()

    def show_title(self):
        return self.title
    
    def __getattr__(self, name):
        print("user __getattr__")
        return getattr(self._data, name)
    
    def __setattr__(self, name, value):
        print("user __setattr__")
        return object.__setattr__(self._data, name, value)

    def __delattr__(self, name):
        print("user __delattr__")
        return object.__delattr__(self._data, name)

    def __getattribute__(self, name):
        if name in ('_data', 'title', 'show_title'):
            return object.__getattribute__(self, name)  # 使用object 而不是self 防止陷入无限循环
        print(f"use __getattribute__ :{name}")
        if name.statswith('b'):
            raise AttributeError
        return object.__getattribute__(self._data, name)

