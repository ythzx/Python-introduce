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