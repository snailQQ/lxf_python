#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def my_abs(x):
    if x < 0:
        return -x
    else:
        return x


print(my_abs(-9))

#参数检查
def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# print(my_abs2('A'))

#返回多个值
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x,y)

#可变参数
# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


#关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

def person2(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)