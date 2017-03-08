# Script Name	: example-16.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-03-07
# Description	: No.16 爬虫的异常处理实战

'''
    爬虫在运行的过程中, 很多时候会遇到这样或那样的异常。如果没有异常处理,爬虫遇到异常时就会直接崩溃停止运行,
    当下次再运行爬虫时,又会重头开始,所以要开发一个具有顽强生命力的爬虫,必须要进行异常处理
'''

# 16.1 认识URLError与HTTPError
'''
    两者都是异常处理的类, HTTPError是URLError的子类,HTTPError有异常状态码与异常原因,URLError没有异常状态码,所以
    在处理时,不能使用URLError代替HTTPError。如果要代替,必须要判断是否有状态码属性
'''

# 16.2 异常处理
'''
    异常出现的原因:
    1. 连不上服务器
    2. 远程url不存在
    3. 无网络
    4. 触发HTTPError
'''

import urllib.request
import urllib.error

try:
    # 当直接请求csdn的博客网站时,会出现403异常,
    # 因为csdn会对爬虫访问进行屏蔽,那么就需要伪装成浏览器才能爬取(后面会补充)
    urllib.request.urlopen("http://blog.csdn.net")
except urllib.error.URLError as e:
    # 捕捉异常,并获取异常code及异常信息
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)