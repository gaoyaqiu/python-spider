# Script Name	: example-11.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-03-05
# Description	: No.11 正则表达式-贪婪模式和懒惰模式

import re

# 贪婪模式和懒惰模式
string = 'pythony'
# 默认就是贪婪模式
pat = "p.*y"

# 懒惰模式
pat = "p.*?y"
rst = re.search(pat, string, re.I)
print(rst)

# 正则函数 re.match()、 re.search()、全局匹配、re.sub()
# match 从头开始匹配
string = 'pythonyjkjkjssa'
pat = "p.*?y"
rst = re.match(pat, string)
print(rst)

# search 从任意地方匹配

# 全局匹配函数
string = 'sdpythpnyonyjkjkjptyssa'
pat = "p.*?y"
rst = re.compile(pat).findall(string)
print(rst)


# 正则表达式 实例
import re

# 匹配.com 和 .cn

string = "<a href='http://www.baidu.com'>百度</a>"

pat = "[a-zA-z]+://[^\s]*[.com|.cn]"

ret = re.compile(pat).findall(string)

print(ret)

# 匹配电话号码
string = "sdfsdfs021-123132432432fsfdwfds0773-23424324234sdfsdfsd"
pat = "\d{3}-\d{8}|\d{4}-\d{7}"
ret = re.compile(pat).findall(string)

print(ret)

