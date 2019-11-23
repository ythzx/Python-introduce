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


# sys
import sys

sys.getrefcount() # 引用计数
sys.getsizeof() # 占用的字节数

for obj in ({}, [], (), 'string', 1, 12.3):
    print(obj.__class__.__name__, sys.getsizeof(d))

# dict 64   
# list 64   
# tuple 64  
# str 64    
# int 64    
# float 64  

# sys.argvs

import sys

script_name, *args = sys.argv  # python3的解包
print(f'Script: {script_name}') # 文件名
print(f'Arguments: {args}') # 传入的参数

# python argv.py -v


# csv

import csv 

with open('test.csv', 'wt') as f:
    writer = csv.writer(f)
    writer.writerow(('id', '用户', '类型'))
    for i in range(3):
        row = (i, f'用户{i}', f'类型{i}')
        writer.writerow(row)
    
with open('test.csv', 'rt') as f:
    reader = csv.DictReader(f)
    for i in reader:
        print(i)

# datetime

import datetime

