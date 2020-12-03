#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。要注意，这里的偏函数和数学意义上的偏函数不一样。

# 在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。举例如下：

# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：

print(int('12345'))
print(int('12345', base=8))
print(int('12345', 16))

def int2(x, base=2):
    return int(x, base)

print(int2('1000000'))

# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
import functools
int22 = functools.partial(int, base=2)
print(int22('1010101'))
