#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 用\d可以匹配一个数字，\w可以匹配一个字母或数字
# '00\d'可以匹配'007'，但无法匹配'00A'；

# '\d\d\d'可以匹配'010'；

# '\w\w\d'可以匹配'py3'；

# .可以匹配任意字符，所以：

# 'py.'可以匹配'pyc'、'pyo'、'py!'等等。
# 要匹配变长的字符，在正则表达式中，用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符：

# 来看一个复杂的例子：\d{3}\s+\d{3,8}。
# 进阶
# 要做更精确地匹配，可以用[]表示范围，比如：

# [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；

# [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；

# [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；

# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。

# A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。

# ^表示行的开头，^\d表示必须以数字开头。

# $表示行的结束，\d$表示必须以数字结束。

# 你可能注意到了，py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了。

# 练习
# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：

# someone@gmail.com
# bill.gates@microsoft.com

import re
def is_valid_email(addr):
    if re.match(r'[0-9a-zA-Z\.]+@[0-9a-zA-Z\.]+', addr):
        return True

def name_of_email(addr):
    m = re.match(r'^<?(\w+\s*\w*)>?(\s*\w*)@(\w+).(\w+)$',addr) 
    print(m)
    if m:
        return m.group(1)

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')