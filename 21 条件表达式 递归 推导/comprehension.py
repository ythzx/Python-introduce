# coding: utf-8

# 列表推导
res1 = [i * i for i in [1,2,3]]
print(res1)

# 带条件的解析
res2 = [i * i for i in [1,2,3] if i % 2 and i %3]
print(res2)


# 集合解析
res3 = {i*i for i in [1,2,3,4,1]}  # 去重
print(res3)

res4 = {k: v*v for k,v in [('a',1), ('b', 2)]}
print(res4)