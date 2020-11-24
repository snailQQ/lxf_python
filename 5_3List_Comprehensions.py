#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
#举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：

list_one = list(range(1, 11))
print(list_one)

print([x * x for x in range(1,11)])

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print([x * x for x in range(1,11) if x % 2 == 0])
#还可以使用两层循环，可以生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])

import os # 导入os模块，模块的概念后面讲到
print([d for d in os.listdir('.')])# os.listdir可以列出文件和目录

#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

#if... else
print([x for x in range(1, 11) if x % 2 == 0])


#这是因为跟在for后面的if是一个筛选条件，不能带else，否则如何筛选？
#另一些童鞋发现把if写在for前面必须加else，否则报错：
print([x if x % 2 == 0 else -x for x in range(1,11)])

#练习
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：

# >>> L = ['Hello', 'World', 18, 'Apple', None]
# >>> [s.lower() for s in L]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <listcomp>
# AttributeError: 'int' object has no attribute 'lower'
# 使用内建的isinstance函数可以判断一个变量是不是字符串：

# >>> x = 'abc'
# >>> y = 123
# >>> isinstance(x, str)
# True
# >>> isinstance(y, str)
# False

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')