#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。

# __slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。

# 除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

# __str__

class Student(object):
    def __init__(self, name):
        self.name = name

    #adding below function
    def __str__(self):
        return 'Student object (name: %s)' % self.name

print(Student('Michael'))
# __main__.Student object at 0x109afb190>

# 但是细心的朋友会发现直接敲变量不用print，打印出来的实例还是不好看：

# >>> s = Student('Michael')
# >>> s
# <__main__.Student object at 0x109afb310>
# 这是因为直接显示变量调用的不是__str__()，而是__repr__()，
# 两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

# __repr__ = __str__

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

# __getitem__

class Fib2(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

# __getattr__

# __call__

#enum class
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# 练习
# 把Student的gender属性改造为枚举类型，可以避免使用字符串：
class Gender(Enum):
    Male = 0
    Female = 1

class Student3(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# metaclass
# type()
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
