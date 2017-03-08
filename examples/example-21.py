# Script Name	: example-21.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-03-08
# Description	: No.21 IP代理池构建实战

import urllib.request
import re
import random

ippools = [
    "42.3.172.188:8998",
    "182.227.98.233:8080",
    "121.135.146.184:8080"
]

def ip(ippools):
    # 此处还可以通过接口获取代理,适合代理不稳定的情况
    thisip = random.choice(ippools)
    print("当前使用的代理: " + thisip)
    proxy = urllib.request.ProxyHandler({"http": thisip})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    # 设定为全局
    urllib.request.install_opener(opener)

for i in range(0, 3):
    ip(ippools)
    url = "http://www.baidu.com"
    data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
    print(data)


