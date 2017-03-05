# Script Name	: example-8.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-03-05
# Description	: No.8 正则表达式-原子


# 8.1 原子
'''
    原子是正则表达式中最基本的组成单位,每个正则表达式中至少要包含一个原子。
    常见的原子类型有:
        a. 普通字符作为原子
        b. 非打印字符作为原子
        c. 通用字符作为原子
        d. 原子表
'''

import re

string = "gaoyaqiu"
# 普通字符作为原子
pat = "gao"

rst = re.search(pat, string)
print(rst)

# 非打印字符作为原子
# \n 换行符 \t 制表符

string = '''gaoyaqiuubaidu'''

pat = "\n"
rst = re.search(pat, string)
print(rst)

# 通用字符作为原子
'''
\w 匹配任意一个字母、数字、下划线
\W 匹配除字母、数字、下划线之外的任意字符
\d 十进制数
\D 除十进制以外的任意字符
\s 匹配空白字符
\S 匹配除空白以外的任意字符
'''
string = '''gaoyaqiu8 76522gaoyaqiubaidu'''

pat = "\w\d\s\d\d"
rst = re.search(pat, string)
print(rst)

# 原子表 从原子表中任意选一个原子来匹配
string = '''gaoyaqiu876522jiaoyubaidu'''

pat = "ga[o]ya"
#pat = "tao[^a]un"
rst = re.search(pat, string)
print(rst)