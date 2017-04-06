# Script Name	: example-24.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-04-06
# Description	: No.24 在Urllib中使用XPath表达式(需要安装lxml模块)

import urllib.request
from lxml import etree

data = urllib.request.urlopen('http://www.baidu.com').read().decode('utf-8', 'ignore')
tree_data = etree.HTML(data)
title = tree_data.xpath('//title/text()')
if(str(type(title) == "<class 'list'>")):
    pass
else:
    # 如果不是列表则转换成列表,防止出错
    title = [i for i in title]

print(title[0])
