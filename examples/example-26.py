# Script Name	: example-26.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-04-18
# Description	: No.26 PhantomJS基础实战
'''
PhantomJS 是一个脚本化的无界面 WebKit，以 JavaScript 为脚本语言实现各项功能，
官方列举的使用场景包括：无界面测试，页面自动化，屏幕截图和网络监控。

需要安装selenium、phantomjs
1. selenium 直接通过pip安装
2. mac下可以使用 brew 来安装 phantomjs
'''
import time
import re
from selenium import webdriver

browser = webdriver.PhantomJS()
# 通过get方式来访问百度
browser.get("http://www.baidu.com/")
# 截屏保存 打开百度后的状态
browser.get_screenshot_as_file("/Users/gaoyaqiu/Downloads/bak/test/baidu.jpg")

# 模拟在百度中搜索
# 先清除文本框
input_xpath = '//*[@id="kw"]'
browser.find_element_by_xpath(input_xpath).clear()
browser.find_element_by_xpath(input_xpath).send_keys('python')
# 截屏保存 在百度中输入 python后的状态
browser.get_screenshot_as_file("/Users/gaoyaqiu/Downloads/bak/test/baidu2.jpg")

#
sub_xpath = '//*[@id="su"]'
browser.find_element_by_xpath(sub_xpath).click()
# 延迟2秒
time.sleep(3)
# 截屏保存 在百度中输入搜索python后的结果
browser.get_screenshot_as_file("/Users/gaoyaqiu/Downloads/bak/test/baidu3.jpg")

# 获取网页源码
data = browser.page_source
print(data)
# 关闭浏览器
browser.quit()

# 获取title
pat = '<title>(.*?)</title>'
title = re.compile(pat).findall(data)
print(title)
