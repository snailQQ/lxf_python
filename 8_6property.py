#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 由于Python是动态语言，根据类创建的实例可以任意绑定属性。

# 给实例绑定属性的方法是通过实例变量，或者通过self变量：
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

# 练习
# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student2(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student2.count +=1

# 测试:
if Student2.count != 0:
    print('测试失败1!')
else:
    bart = Student2('Bart')
    if Student2.count != 1:
        print(bart.count)
        print('测试失败2!')
    else:
        lisa = Student2('Bart')
        if Student2.count != 2:
            print('测试失败3!')
        else:
            print('Students:', Student2.count)
            print('测试通过!')