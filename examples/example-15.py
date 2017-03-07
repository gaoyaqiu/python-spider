# Script Name	: example-15.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-03-07
# Description	: No.15 自动模拟HTTP请求之自动POST实战


# post请求实战
import urllib.request
import urllib.parse

# 这里使用了apache的一个post测试地址
posturl = "http://httpbin.org/post"
# post请求的参数, 当参数中有中文时,记得需要做encode处理
postdata = urllib.parse.urlencode({
    "name": "张三",
    "age": 18
}).encode("utf-8")

req = urllib.request.Request(posturl, postdata)
rst = urllib.request.urlopen(req).read().decode("utf-8")
print(rst)

'''
返回的结果如下: 其中form对应的值就是在我请求时传入的参数
{
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "age": "18",
    "name": "\u5f20\u4e09"
  },
  "headers": {
    "Accept-Encoding": "identity",
    "Content-Length": "30",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "httpbin.org",
    "User-Agent": "Python-urllib/3.5"
  },
  "json": null,
  "origin": "116.226.186.125",
  "url": "http://httpbin.org/post"
}

'''