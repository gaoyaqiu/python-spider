# Script Name	: example-6.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-03-05
# Description	: No.6 python异常处理实战

# 6.1 异常处理概述
# python程序在执行的时候,经常会遇到异常,如果中间异常不处理,经常会导致程序崩溃。
# 比如后面我们写爬虫的时候,如果不进行异常处理,很可能虫爬了一半,直接崩溃了。

# 6.2 异常处理格式
'''
    try:
        程序
    except Exception as 异常名称:
        异常处理部分
'''
'''
try:
    for i in range(0, 10):
        print(i)
        if(i == 4):
            print(nihao)
except Exception as e:
    print(e)
# 让异常后的程序继续执行

for i in range(0, 10):
    try:
        print(i)
        if(i == 4):
            print(nihao)
    except Exception as e2:
        print(e2)
print("ok")

'''

for i in range(0, 10):
    try:
        print(i)
        if(i == 4):
            print(nihao)
    except Exception as e2:
        print(e2)
