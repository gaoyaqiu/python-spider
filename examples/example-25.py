# Script Name	: example-25.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-04-17
# Description	: No.25 BeautifulSoup基础实战
'''
BeautifulSoup 是 Python 非常好用的一个库，可以用它来方便地解析网页内容，获取我们需要的数据，几乎是 Python 爬虫居家旅行必备的库,
和正则、xpath作用是一样的,主要作用是简化开发。
使用之前需要安装beautifulsoup库, 选择自己对应的python版本
下载地址: http://www.lfd.uci.edu/~gohlke/pythonlibs/
'''

import urllib.request
from bs4 import BeautifulSoup as bs

data = urllib.request.urlopen("https://www.douban.com/").read().decode("utf-8", "ignore")
# 解析数据(常用的解析器有: html.parser、lxml、["lxml", "xml"]、html5lib), 这里我们用 html.parser
bs_data = bs(data, "html.parser")
#print(bs_data)

# 格式化输出html (比较美观)
#print(bs_data.prettify())

# 获取标签
print(bs_data.title)

# 获取标签中的内容
print(bs_data.title.string)

# 获取标签名
print(bs_data.title.name)

# 获取属性列表(默认获取的是第一个标签)
print(bs_data.a.attrs)

# 获取属性对应的值 (下面两种方式都可以)
print(bs_data.a['class'])
print(bs_data.a.get('class'))

# 获取某个节点的所有内容(多个标签可以传入数组)
#print(bs_data.find_all('a'))
#print(bs_data.find_all(['a', 'ul']))

# 获取所有子节点 (contents返回的是list, children返回的是iterator)
print(bs_data.ul.contents)
#print(bs_data.ul.children)
t = bs_data.ul.children
#for i in t:
   # print(i)

# iterator转为list
t2 = [i for i in t]
print(t2)


# 更多使用帮助请参阅官方文档: http://beautifulsoup.readthedocs.io/zh_CN/latest/


