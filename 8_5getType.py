#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？

# 使用type()
# 首先，我们来判断对象类型，使用type()函数：

# 基本类型都可以用type()判断：

print(type(123))
print(type('str'))
print(type(None))
print(type(abs))

# 使用isinstance()
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。

# 我们回顾上次的例子，如果继承关系是：

# object -> Animal -> Dog -> Husky
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir('ABC'))
print(len('ABC'))
print('ABC'.__len__())

class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))

print('ABC'.lower())

# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：

# >>> class MyObject(object):
# ...     def __init__(self):
# ...         self.x = 9
# ...     def power(self):
# ...         return self.x * self.x
# ...
# >>> obj = MyObject()
# 紧接着，可以测试该对象的属性：

# >>> hasattr(obj, 'x') # 有属性'x'吗？
# True
# >>> obj.x
# 9
# >>> hasattr(obj, 'y') # 有属性'y'吗？ 
# False
# >>> setattr(obj, 'y', 19) # 设置一个属性'y'
# >>> hasattr(obj, 'y') # 有属性'y'吗？
# True
# >>> getattr(obj, 'y') # 获取属性'y'
# 19
# >>> obj.y # 获取属性'y'
# 19