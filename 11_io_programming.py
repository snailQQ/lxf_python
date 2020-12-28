#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 同步IO
# 异步IO
# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：

# try:
#     f = open('/path/to/file', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：

# with open('/path/to/file', 'r') as f:
#     print(f.read())
# 
# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
