# Script Name	: example-13.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-03-05
# Description	: No.13 超时设置

# 由于网络速度或对方服务器问题, 爬取一个网页的时候,都需要时间。如果该网页长时间未响应,
# 那么系统就会判断该网页超时,有时我们就需要根据需要来设置超时时间值
# 比如我们希望2秒没有反应,则判断为超时,那么timeout值就是2,再比如,有些网站服务器比较慢,那么我们希望100秒没有响应时,
# 才判断为超时, 那么此时timeout值设置为100.

# 超时设置
import urllib.request

for i in range(0, 100):
    try:
        # 测试可以选用一个网站响应比较慢的来测试效果
        file = urllib.request.urlopen("http://tool.360java.com", timeout=1)
        print(file.read().decode("utf-8"))
    except Exception as err:
        print("出现异常: " + str(err))

