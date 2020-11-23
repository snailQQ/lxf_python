# print absolute value of an integer:
a = 100
if a >= 0:
    print(a)
else:
    print(-a)

print('I\'m ok.')

# -------------------

# >>> print('\\\t\\')
# \       \
# >>> print(r'\\\t\\')
# \\\t\\
print('\\\t\\')
print(r'\\\t\\')

print('''line1
... line2
... line3''')

# ----------------------

# >>> print(r'''hello,\n
# ... world''')
# hello,\n
# world
# >>> print('''hello,\n
# ... world''')
# hello,

# world

# ------------------

a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)

# ------------------

a = 'ABC'
b = a
a = 'XYZ'
print(b)

# ------------------常量
print(10 / 3)
print(9 / 3)
print(10 // 3)
print(10 % 3)

# ------------------练习
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print('n: ', n)
print('f: ', f)
print('s1: ', s1)
print('s2: ', s2)
print('s3: ', s3)
print('s4: ', s4)

# ------------------编码
print('包含中文的str')
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print('\u4e2d\u6587')
#Python对bytes类型的数据用带b前缀的单引号或双引号表示：
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
#print('中文'.encode('ascii'))
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
print(len('ABC'))
print(len('中文%'))
print('%')

# >>> len(b'ABC')
# 3
# >>> len(b'\xe4\xb8\xad\xe6\x96\x87')
# 6
# >>> len('中文'.encode('utf-8'))
# 6


# >>> 'Hello, %s' % 'world'
# 'Hello, world'
# >>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
# 'Hi, Michael, you have $1000000.'

# >>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
# 'Hello, 小明, 成绩提升了 17.1%'


s1 = 72
s2 = 85
r = (s2 / s1 - 1) * 100
print(r)
print('score increaced %% is: %.1f %%' % r, '%')

# ------------------list and tuple
# ------------------条件判断
# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>