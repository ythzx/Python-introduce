



## 可迭代对象

定义返回迭代器的__iter__方法或者支持下标索引的__item__方法就是一个可迭代对象



```python
In [1]: l = [1,2,3]

In [2]: l.__iter__
Out[2]: <method-wrapper '__iter__' of list object at 0x000001845F79A288>

In [3]: next(l)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-cdc8a39da60d> in <module>
----> 1 next(l)

TypeError: 'list' object is not an iterator

In [4]: l2 = iter(l)

In [5]: next(l2)
Out[5]: 1

In [6]: next(l2)
Out[6]: 2

In [7]: next(l2)
Out[7]: 3

In [8]: next(l2)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-8-37611c3e7a32> in <module>
----> 1 next(l2)
In [9]: l2
Out[9]: <list_iterator at 0x1845f77af98>
```

list 对象l 有__iter__ 但是不是迭代器
使用iter() 变成迭代器
使用next() 调用最后会抛出Stopiteration异常

## 迭代器

实现了`__iter__`和next方法的对象就是迭代器

`__iter__` 返回迭代器对象本身，next 返回容器的下一个元素，杂偶没有后续元素时抛出StopIteration异常

> Python2 中next方法定义为`__next__`


