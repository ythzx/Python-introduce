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
subject = Subject(1, 1000,'条目1')

# 获取对象的属性
print(subject.kind, subject.id, subject.category_id,subject.title)

# 调用对象的方法
res = subject.show_title()
print(res)

# 方法会更新对象属性
subject.update_title('new title')
res1 = subject.show_title()
res2 = subject.title
print(res1, res2)
