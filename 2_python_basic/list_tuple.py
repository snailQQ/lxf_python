#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#list list是一种有序的集合，可以随时添加和删除其中的元素。
classmate = ['Michael', 'Bob', 'Tracy']
print(classmate)
print(len(classmate))
print(classmate[0])
print(classmate[1])
print(classmate[2])
print(classmate[-1])
classmate.append('Adam')
print(classmate)
classmate.insert(1, 'Jack')
print(classmate)
print(classmate.pop())
print(classmate)
print(classmate.pop(1))
print(classmate)
classmate[1] = 'Sarah' #可以通过直接赋值来替换list里的元素
print(classmate)

L = ['Apple', 123, True] #list里的元素可以是不同数据类型
print(L)

#list元素也可以是另一个list
s=['python', 'java', ['asp', 'php'], 'scheme']
print(s)
print(len(s))

#等同于
p1 = ['asp', 'php']
p2 = ['python', 'java', p1, 'scheme']
print(p2[2][1])

L_empty = []
print(len(L_empty))

#tuple 元组
#tuple 是一种有序序列。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字
classmates_tuple = ("Michael", 'Bob', 'Tracy')
print(classmates_tuple)

#tuple 一旦初始化以后就不能修改了。也没有append()，insert()等方法. 其他获取元素的方法和list是一样的.
print(classmates_tuple[1])
print(classmates_tuple[-1])
t = (1,2)
print(t)
t = ()
print(t)
print(len(t))
#定义一个空的tuple，可以写成(), 但是，要定义一个只有1个元素的tuple 定义的不是tuple，是1这个数！
# 这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，
# 因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
t = (1)
print(t)
#所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)
print(t)
print(len(t))

t = ('a', 'b', ['A','B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

#practice
# -*- coding: utf-8 -*-

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])










