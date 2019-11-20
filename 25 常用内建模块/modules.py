import os

os.getcwd() # 获取当前路径

os.chdir('..') # 切换到上级目录

# 获取环境变量
os.getenv('path') 
os.environ.get('path')

os.listdir()

os.walk('dir') # 迭代器

list(os.walk('dir'))

# 创建文件夹
os.mkdir('dirname')

# 创建多级文件夹
os.makedirs('dir1/dir2')

# 删除文件
os.remove('1.txt')

# 重命名
os.rename('dir1', 'dir2')

"""
os.path
"""
p = 'C:/Users/admin/Desktop/1.txt'
os.path.basename(p) # 获取指定路径文件名字

os.path.dirname(p) # 获取指定文件路径名字

os.path.exists(p) # 判断文件或者路径是否存在

