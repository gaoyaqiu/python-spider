# Script Name	: example-18.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-03-08
# Description	: No.18 CSDN博文爬虫


import urllib.request
import re

url = "http://blog.csdn.net/"
headers = ("User-Agen","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
# 设定为全局
urllib.request.install_opener(opener)
data = opener.open(url).read().decode("utf-8")
pat = '<h3  class="tracking-ad" data-mod="popu_254"><a href="(.*?)"'
alllink = re.compile(pat).findall(data)

# 如果本地测试,需要修改成自己的电脑路径
localpath = "/Users/gaoyaqiu/Downloads/python-test/18/"
if(len(alllink)):
    for i in range(0, len(alllink)):
        currlink = alllink[i]
        # 将文章下载到本地目录

        urllib.request.urlretrieve(currlink, localpath + str(i) + ".html")
        print("当前文章为,第" + str(i+1) + "篇, 爬取成功!")