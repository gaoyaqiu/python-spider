# Script Name	: example-12.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-03-05
# Description	: No.12 简单爬虫的编写(urllib学习)

import urllib.request
import re

data = urllib.request.urlopen("http://edu.csdn.net").read()

#print(data)

# 自动提取课程页面的QQ群号码
data = urllib.request.urlopen("http://edu.csdn.net/huiyiCourse/detail/253").read().decode("utf-8")
pat = "<p>(\d*?)</p>"
ret = re.compile(pat).findall(data)
print(ret[0])

# 豆瓣网址出版爬取

'''
import urllib.request
import re

data = urllib.request.urlopen("https://read.douban.com/provider/all").read().decode("utf-8")
pat = '<div class="name">(.*?)</div>'
ret = re.compile(pat).findall(data)

fh = open("/Users/gaoyaqiu/git/python-demo/douban", "w")
for i in range(0, len(ret)):
    print(ret[i])
    fh.write(ret[i] + "\n")
fh.close()

'''


import urllib.request

# urlretrieve(网址, 存储位置) 直接下载网页到本地

#urllib.request.urlretrieve("http://www.baidu.com", "/Users/gaoyaqiu/git/python-demo/baidu.html")

# urlcleanup() 清除由于urllib.urlretrieve()所产生的缓存
# urllib.request.urlcleanup()

# info() 查看网页简介信息
'''
Date: Sat, 04 Mar 2017 12:09:02 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 61320
Connection: close
Vary: Accept-Encoding
Expires: Sun, 1 Jan 2006 01:00:00 GMT
Pragma: no-cache
Cache-Control: must-revalidate, no-cache, private
Set-Cookie: profile="deleted"; max-age=0; domain=read.douban.com; expires=Thu, 01-Jan-1970 00:00:00 GMT; path=/
Set-Cookie: bid=bKnd76QHTVg; Expires=Sun, 04-Mar-18 12:09:02 GMT; Domain=.douban.com; Path=/
X-DOUBAN-NEWBID: bKnd76QHTVg
X-DAE-Node: sindar20d
X-DAE-App: ark
Server: dae
Strict-Transport-Security: max-age=15552000;
X-Content-Type-Options: nosniff
'''
file = urllib.request.urlopen("https://read.douban.com/provider/all")
print(file.info())

# getcode() 返回网站状态码 200
print(file.getcode())

# geturl() 获取当前访问的url
print(file.geturl())

