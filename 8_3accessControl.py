#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。

# 但是，从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性：

# >>> bart = Student('Bart Simpson', 59)
# >>> bart.score
# 59
# >>> bart.score = 99
# >>> bart.score
# 99
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
# 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

# 练习
# 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：

class Student2(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    
    def get_gender(self):
        return self.__gender
    
    def set_gender(self, gender):
        self.__gender = gender

# 测试:
bart2 = Student2('Bart', 'male')
if bart2.get_gender() != 'male':
    print('测试失败!')
else:
    bart2.set_gender('female')
    if bart2.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
