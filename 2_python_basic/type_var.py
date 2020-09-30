#print absolute value of an integer:
a = 100
if a >= 0:
    print(a)
else:
    print(-a)


print('\\\t\\')
#\  \

#Python还允许用r''表示''内部的字符串默认不转义
print(r'\\\t\\')

#Python允许用'''...'''的格式表示多行内容
print('''line1
line2
line3''')

print(r'''hello 
world''')

print(True)
print('True')

#在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
a = 123
print(a)
a = "ABC"
print(a)

#int b = 123
#b = 'ABC'
a = 'ABC'
b = a
a = 'XYZ'
print(b)

#除法
print(10 / 3)
print(10 // 3)
print(10 % 3)

# 练习
# 请打印出以下变量的值：

# # -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print(n)
print(f)
print(s1)
print('Hello,\\\'Adam\\\'')
print(s3)
print(s4)
print('s4 = r\'\'\'Hello,\nLisa!\'\'\'')