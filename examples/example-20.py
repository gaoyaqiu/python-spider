# Script Name	: example-20.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-03-08
# Description	: No.20 用户代理池构建实战

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
    print(thisua)
    headers = ("User-Agen", thisua)
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    # 设定为全局
    urllib.request.install_opener(opener)


for i in range(0, 5):
    ua(proxy)
    thisurl = "http://www.qiushibaike.com/8hr/page/" + str(i+1) + "/"
    data = urllib.request.urlopen(thisurl).read().decode("utf-8", "ignore")
    pat = '<div>.*?<span>(.*?)</span>.*?</div>'
    rst = re.compile(pat, re.S).findall(data)
    for i in range(0, len(rst)):
        print(rst[i])
        print("-----------------------------")
