# Script Name	: example-4.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-03-05
# Description	: No.4 python模块实战


# 4.1 什么是模块?
# 为了让python程序实现起来更方便,我们可以按需求类别将一些常见的功能(函数)组合在一起,形成模块。以后我们要实现这一类功能的时候,直接
# 导入该模块即可。模块里面的函数叫做模块的方法

# 4.2 python 模块的导入
# 使用以下两种方式导入模块:
# a. import 模块名
# b. from ... import ...

# 例子(import 模块名)
import cgi
# 执行cgi中得方法
cgi.closelog()

# 例子(from ... import ...)

from cgi import closelog
# 直接执行closelog方法
closelog()

# 4.3 第三方模块的安装
# a. pip方式
# b. whl下载安装的方式
# c. 直接复制的方式
# d. anaconda

# 4.4 自定义python模块
# 创建mymd.py文件,将以下代码拷贝进去
def hello():
    print("hello python!")

# 将mymd.py文件放入python安装目录的Lib下(系统的内置的模块也在这)

# 使用自定义模块
# import mymd

# 调用mymd下的hello方法
# mymd.hello()
# 或者用 from mymd import hello
