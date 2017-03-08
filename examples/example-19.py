# Script Name	: example-19.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-03-08
# Description	: No.19 糗事百科段子爬虫

import urllib.request
import re

headers = ("User-Agen","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
# 设定为全局
urllib.request.install_opener(opener)

for i in range(0, 1):
    thisurl = "http://www.qiushibaike.com/8hr/page/" + str(i+1) + "/"
    data = urllib.request.urlopen(thisurl).read().decode("utf-8", "ignore")
    pat = '<div>.*?<span>(.*?)</span>.*?</div>'
    rst = re.compile(pat, re.S).findall(data)
    for i in range(0, len(rst)):
        print(rst[i])
        print("-----------------------------")
