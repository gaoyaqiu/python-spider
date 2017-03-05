# Script Name	: example-5.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-03-05
# Description	: No.5 python文件操作实战


# 5.1 读取文件
# 打开文件
# open(文件名, 操作形式)
'''
w: 写入
r: 读取
b: 二进制
a: 追加
'''
fh = open("/Users/gaoyaqiu/Downloads/t1", "r")
# 文件读取可以用read(读取文件所有内容)和readline(按行读取)方法
# data = fh.read()

while True:
    line = fh.readline()
    print(line)
    if not line:
        break
    pass

# 关闭文件
fh.close()

# 5.2 文件写入
data = "hello world"
fh2 = open("/Users/gaoyaqiu/Downloads/t2", "w")
fh2.write(data)
fh2.close()

data2 = "gyq"
fh2 = open("/Users/gaoyaqiu/Downloads/t2", "a+")
fh2.write(data2)
fh2.close()

