#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#在Python中，迭代是通过for ... in来完成的，而很多语言比如C语言，迭代list是通过下标完成的

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
#因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。

for value in d.values():
    print(value)

for letter in 'ABC':
    print(letter)

# from collections import Iterable
# print(isinstance('abc', Iterable))
# print(isinstance([1,2,3], Iterable))
# print(isinstance(123, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

#练习
#请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    v_min = None
    v_max = None
    for elment in L:
        if not v_min or elment < v_min:
            v_min = elment
        if not v_max or elment > v_max:
            v_max = elment
    return(v_min, v_max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')