# Script Name	: example-17.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-03-07
# Description	: No.17 爬虫的浏览器伪装技术实战

'''
    由于urlopen()对于一些HTTP的高级功能不支持,所以,我们如果要修改报头,可以使用urllib.request.build_opener()进行,还有一种方法之前有写过,就是
    urllib.request.Request()下的add_header()方法来实现浏览器的模拟,这里主要学习前者build_opener的方式
'''

# 17.1 浏览器伪装
import urllib.request

url = "http://blog.csdn.net"

# 设置头部信息, 头部信息可以通过浏览器查看获得,这里主要以谷歌浏览器为例,按F12,查看Network,选中一个网络请求,复制User-Agent对应的值
headers = ("User-Agen","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]

data = opener.open(url).read().decode("utf-8")
print(data)