# coding: utf-8

f = open('note.txt','r')
# line = f.readline()
# print(line)

# lines = f.readlines()
# lines1 = f.readlines()

# print(lines)
# print(lines1)
# print(f.tell())  # 返回文件读取指针位置
# print(f.seek(3))
# lines2 = f.readlines()
# print(lines2)
# print(f.read(4096))
for line in f:
    print(line, end='')