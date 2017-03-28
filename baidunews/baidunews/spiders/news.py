# -*- coding: utf-8 -*-
import scrapy

from baidunews.items import BaidunewsItem
import re
from scrapy.http import Request

class NewsSpider(scrapy.Spider):
    name = "news"
    #allowed_domains = ["baidu.com"]
    start_urls = ['http://baidu.com/']
    # 网站分类
    allid = ['LocalHouseNews', 'LocalNews']
    # 构造请求地址
    allurl = []
    for i in range(0, len(allid)):
        thisurl = "http://news.baidu.com/widget?id=" + allid[i] + "&ajax=json"
        allurl.append(thisurl)
    def parse(self, response):
            for j in range(0, len(self.allurl)):
                print("正在爬取第" + str(j) + "个栏目")
                yield Request(self.allurl[j], callback = self.getData1)
    # 处理爬取到的数据
    def getData1(self, response):
        data = response.body.decode('utf-8', 'ignore')
        pat1 = '"m_relate_url":"(.*?)"'
        pat2 = '"url":"(.*?)"'
        # 提取json串中的文章url地址
        url1 = re.compile(pat1, re.S).findall(data)
        url2 = re.compile(pat2, re.S).findall(data)
        if(len(url1) != 0):
            url = url1
        else:
            url = url2
        for k in range(0, len(url)):
            articleurl = url[k]
            # 处理url中转义符号\/\/
            articleurl = re.sub('\\\/', '/', articleurl)
            yield Request(articleurl, callback = self.getData2)
    def getData2(self, response):
         item = BaidunewsItem()
         item['link'] = response.url
         item['title'] = response.xpath("/html/head/title/text()").extract()
         item['content'] = response.body
         yield item