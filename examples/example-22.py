# Script Name	: example-22.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-03-09
# Description	: No.22 淘宝商品图片爬虫实战

import urllib.request
import re
import random

proxy = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
]

# 随机切换用户代理池
def ua(proxy):
    thisua = random.choice(proxy)
    print("当前使用的用户代理: " + thisua)
    headers = ("User-Agen", thisua)
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    # 设定为全局
    urllib.request.install_opener(opener)

keyword = "iphone"
keyword = urllib.request.quote(keyword)
for i in range(1, 2):
    ua(proxy)

    thisurl = "https://s.taobao.com/search?q=" + keyword + "&s=" + str((i-1) * 44)
    data = urllib.request.urlopen(thisurl).read().decode("utf-8", "ignore")
    pat = '"pic_url":"//(.*?)"'
    imglist = re.compile(pat).findall(data)
    #print(imglist)
    for j in range(0, len(imglist)):
        thisimg = imglist[j]
        thisimgurl = "http://" + thisimg
        localfile = "/Users/gaoyaqiu/Downloads/python-test/22/" + str(i) + str(j) + ".jpg"
        urllib.request.urlretrieve(thisimgurl, localfile)