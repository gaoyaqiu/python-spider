# Script Name	: example-10.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-03-05
# Description	: No.10 正则表达式-模式修正符

# 模式修正符
'''
I 匹配时忽略大小写 *
M 多行匹配 *
L 本地化识别匹配
U unicode
S 让.匹配包括换行符 *
'''
import re

string = 'Python'

pat = "pyt"
rst = re.search(pat, string, re.I)
print(rst)

