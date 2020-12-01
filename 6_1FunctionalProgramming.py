#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。

# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数
# 函数式编程最重要的概念就是：组合；

# 一个函数只做一件事， 保证内部不被修改，且干净，无副作用，遵循开闭原则，然后将多个函数组合一起，便是简单的函数式编程范式；


#Higher-order function
#变量可以指向函数
print(abs(-10))

f = abs
print(f(-10))

#函数名也是变量
# abs = 10
# print(abs)

#传入函数
#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x, y, f):
    return f(x) + f(y)


print(add(-1,-2,abs))

#map / reduce
# Python内建了map()和reduce()函数。

# 如果你读过Google的那篇大名鼎鼎的论文“MapReduce: Simplified Data Processing on Large Clusters”，你就能大概明白map/reduce的概念。

# 我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

# 举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：

#             f(x) = x * x

#                   │
#                   │
#   ┌───┬───┬───┬───┼───┬───┬───┬───┐
#   │   │   │   │   │   │   │   │   │
#   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼

# [ 1   2   3   4   5   6   7   8   9 ]

#   │   │   │   │   │   │   │   │   │
#   │   │   │   │   │   │   │   │   │
#   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼

# [ 1   4   9  16  25  36  49  64  81 ]

def mapFun(x):
    return x * x

r = map(mapFun, [1,2,3,4,5,6,7,8,9])
print(list(r))

# 所以，map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串
print(list(map(str, [1,2,3,4,5,6,7,8,9])))

# 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 比方说对一个序列求和，就可以用reduce实现：
from functools import reduce
def reduceAdd(x, y):
    return x + y

print(reduce(reduceAdd, [1,3,5,7,9]))

def fn(x, y):
    return x * 10 + y

print(reduce(fn, [1,3,5,7,9]))

def char2sum(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(reduce(fn, map(char2sum, '13579')))


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

# 还可以用lambda函数进一步简化成：
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

# 练习
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
NAMES = ['adam', 'LISA', 'barT']
def normalize(name):
    return name[:1].capitalize() + name[1:].lower()

print(list(map(normalize, NAMES)))


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

# # -*- coding: utf-8 -*-
# from functools import reduce
def prod(L):
    return reduce(lambda x, y : x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# filter
# Python内建的filter()函数用于过滤序列。

# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# 例如，在一个list中，删掉偶数，只保留奇数，可以这么写：
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


# 用Python来实现这个算法，可以先构造一个从3开始的奇数序列：

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
# 注意这是一个生成器，并且是一个无限序列。

# 然后定义一个筛选函数：

def _not_divisible(n):
    return lambda x: x % n > 0
# 最后，定义一个生成器，不断返回下一个素数：

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
# 这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。

# 由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：

# # 打印1000以内的素数:
for n in primes():
    if n < 20:
        print(n)
    else:
        break
# 注意到Iterator是惰性计算的序列，所以我们可以用Python表示“全体自然数”，“全体素数”这样的序列，而代码非常简洁。

# 练习
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

# -*- coding: utf-8 -*-
# def is_palindrome(n):


# sorted
# Python内置的sorted()函数就可以对list进行排序：
print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))