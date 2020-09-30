#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
ord('A')
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))

#Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'ABC'
print(x)
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(len('ABC'))
print(len('中文'))
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

#---格式化---
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' %('Michael', 10000))
#%d integer
#%f float
#%s string
#%x hex integer

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print('Age: %s. Gender: %s' % (25, True))
print('growth rate: %d %%' % 7)

#format()
#另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

#f-string
#最后一种格式化字符串的方法是使用以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换：
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')

#practice
#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1 = 72
s2 = 85
print('小明成绩提升 %.1f%%' % ((85/72-1) * 100))
print('小明成绩提升 {0:.1f}%'.format((85/72-1) * 100))
print(f'小明成绩提升 {(85/72-1) * 100:.1f}%')