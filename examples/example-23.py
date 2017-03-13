# Script Name	: example-23.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-03-13
# Description	: No.23 如何同时使用用户代理池和IP代理池

import urllib.request
import re
import random
def ua_ip(url):
    proxy = [
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    ]

    # 网上找的代理
    ippools = [
        "222.128.80.28:8081",
        "218.241.181.202:8080",
        "61.182.253.72:8081"
    ]

    # 随机切换用户代理及IP
    def ip(ippools, proxy):
        thisua = random.choice(proxy)
        print("当前使用的用户代理: " + thisua)
        thisip = random.choice(ippools)
        print("当前使用的IP: " + thisip)
        headers = ("User-Agen", thisua)
        proxy = urllib.request.ProxyHandler({"http": thisip})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        opener.addheaders = [headers]
        # 设定为全局
        urllib.request.install_opener(opener)

    for i in range(0, 5):
        try:
            ip(ippools, proxy)

            thisurl = url
            data = urllib.request.urlopen(thisurl).read().decode("utf-8", "ignore")
            if data:
                return data
        except Exception as e:
            print(e)

url = "http://www.baidu.com"
data = ua_ip(url)
print(data)