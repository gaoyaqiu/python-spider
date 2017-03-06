# Script Name	: example-14.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-03-06
# Description	: No.14 自动模拟HTTP请求与百度信息自动搜索爬虫实战


# 客户端如果要与服务器进行通讯, 需要通过http请求进行, http请求有很多种, 这里主要会对post和get两种方式进行学习
# get请求实战-- 实现百度信息自动搜索
import urllib.request
import re

keyword = "python"
keyword = urllib.request.quote(keyword)

# 分页获取10页数据 page = (num - 1) * 10
for i in range(1, 11):
    url = "https://www.baidu.com/s?wd=" + keyword + "&pn=" + str((i - 1) * 10)
    req = urllib.request.Request(url)
    # 必须要设置user-agent,不然获取不到数据
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
    data = urllib.request.urlopen(req).read().decode("utf-8")
    pat1 = "title:'(.*?)',"
    pat2 = 'title:"(.*?)",'
    rst1 = re.compile(pat1).findall(data)
    rst2 = re.compile(pat2).findall(data)

    for j in range(0, len(rst1)):
        print(rst1[j])

    for z in range(0, len(rst2)):
        print(rst2[z])

