#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Python中非常有用的高级特性，1行代码能实现的功能，决不写5行代码。请始终牢记，代码越少，开发效率越高。

#切片 tuple
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#get 3 elements

#两个不太好的方法
#1
print([L[0], L[1], L[2]])

#2
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)

#python的方法
print(L[0:3])
#0表示从0开始， 3表示到index 3为止，不包括3
print(L[:3])
print(L[1:2]) #从1开始到2为止，打印Sarah
print(L[-2:]) #
print(L[-2:-1]) #


#创建0-99的数列
NL = list(range(100))
print(NL)
print(NL[:10])
print(NL[-10:])
print(NL[10:20])
#前十的数字每两个取一个
print(NL[:10:2])
#所有的数字每五个取一个
print(NL[::5])
print(NL[:])
#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
print((0, 1, 2, 3, 4, 5)[:3])
#字符串也可以看成是list，所有tuple的操作也可以用于字符串
print(['ABCDEF'[:3]])
print('ABCDEFG'[::2])

#练习
#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
print(len("asd   "))
def trim(s):
    while(s[:1] == " "):
        s = s[1:]
    while(s[-1:] == " "):
        s = s[0:-1]
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')
