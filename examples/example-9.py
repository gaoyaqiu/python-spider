# Script Name	: example-9.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-03-05
# Description	: No.9 正则表达式-元字符

# 8.1 元字符
'''
    所谓元字符, 就是正则表达式中具有一些特殊含义的字符, 比如重复N次前面的字符等
'''

import re

'''
. 除换行外任意一个字符
^ 开始位置
$ 结束位置
* 前面原子重复出现0次、1次或多次
? 前面原子重复出现0次、1次
+ 前面原子出现1次或多次
{n} 前面原子恰好出现n次
{n,} 前面原子至少n次
{n, m} 最少出现n次,最多出现m次
| 模式选择符 或
() 模式单元
'''
string = '''taogaoyaqiu876522gaobaidu'''

pat = "tao..."
pat = "^tao..."
pat = "ba...$"
pat = "tao.*"
pat = "taogao+"
pat = "gao{3,5}"
rst = re.search(pat, string)
print(rst)




