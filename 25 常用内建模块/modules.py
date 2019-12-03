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
    print(obj.__class__.__name__, sys.getsizeof(obj))

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

now = datetime.datetime.now()

now.month, now.day, now.hour

today = datetime.datetime.today()

today.year, today.day

dl = datetime.date()

# datetime.timedelta(seconds =1)
# Out[144]: datetime.timedelta(0, 1)

# In [145]: datetime.timedelta(minutes=1)
# Out[145]: datetime.timedelta(0, 60)

# In [146]: datetime.timedelta(hours=1)
# Out[146]: datetime.timedelta(0, 3600)

# In [147]: datetime.timedelta(days=1)
# Out[147]: datetime.timedelta(1)

# In [148]: datetime.timedelta(weeks=1)
# Out[148]: datetime.timedelta(7)

# 格式化

dt_format = "%Y-%m-%d %H:%M:%S"
s = datetime.datetime.now().strftime(dt_format)

s = '2019-11-23 22:35:24'

d = datetime.datetime.strptime(s, dt_format)

# random 
for i in range(5):
    print(f'{random.random():.4f}', end='\t')
    print(f'{random.unifrom(50, 60):.4f}', end='\t')
    print(f'{random.randint(1, 100):.4f}', end='\t')  # 整数范围

for i in range(5):
    print(f'{random.randrange(0,101,1):.4f}', end='\t')

for i in range(5):
    print(f'{random.randrange(0,101,1):.4f}', end='\t')


print(f'{random.sample(range(10), 3)}', end='\t')
print(f'{random.choices(range(10), k=3)}', end='\t')


# logging

import logging

"""
日志级别: value
------------
CRITICAL: int 70
FATAL: int 60 
ERROR: int 50 
WARNING: int 40 
WARN: int 30 
INFO: int 20 
DEBUG: int 10 
NOTSET: int 0 
"""

# stream
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger('test1 loggger')
logger.info("this is info")

logger = logging.getLogger('LGESL')
logger.setLevel(level=logging.INFO)


# file

logging.basicConfig(filename='test.log', level=logging.INFO)
logging.info('started')
logging.info(logging.root.handlers)

# ipython 中使用logging file 的方案

logging.root.setLevel(logging.INFO)

# 最佳使用logging的方案
import logging

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
