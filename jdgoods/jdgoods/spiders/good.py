# -*- coding: utf-8 -*-
# Scrapy与Urllib的整合使用（爬取京东图书商品）
import scrapy
import urllib.request
import re
import random
from jdgoods.items import JdgoodsItem
from scrapy.http import Request


class GoodSpider(scrapy.Spider):
    name = "good"
    allowed_domains = ["jd.com"]
    #start_urls = ['http://jd.com/']

    def start_requests(self):
        proxy = [
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)"
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
        ]

        req1 = urllib.request.Request("http://book.jd.com/")
        # 浏览器伪装
        req1.add_header("User-Agent", random.choice(proxy))
        p_data = urllib.request.urlopen(req1).read().decode("utf-8", "ignore")
        # 匹配渠道的正则
        pat1 = '<h3><a href="..(channel.jd.com/.*?.html)"'
        all_channel = re.compile(pat1).findall(p_data)
        #print(all_channel)
        # 所有的分类id
        cat_all_data = []
        for i in all_channel:
            this_channel_url = "http://" + i
            req2 = urllib.request.Request(this_channel_url)
            req2.add_header("User-Agent", random.choice(proxy))
            this_channel_data = urllib.request.urlopen(req2).read().decode("utf-8", "ignore")
            pat2 = 'href="..list.jd.com.list.html.cat=([0-9,]*?)[&"]'
            cat_data = re.compile(pat2).findall(this_channel_data)
            for j in cat_data:
                cat_all_data.append(j)
        # 去重
        cat_all_data = set(cat_all_data)
        # 每个分类对应的总页数 [{"分类": "页数"}]
        all_page = []
        # 测试控制爬取次数
        n = 0
        # 获取每个分类对应的分页总数
        for k in cat_all_data:
            this_cat_url = "http://list.jd.com/list.html?cat=" + k
            req3 = urllib.request.Request(this_cat_url)
            req3.add_header("User-Agent", random.choice(proxy))
            list_data = urllib.request.urlopen(req3).read().decode("utf-8", "ignore")
            pat3 = "<em>共<b>(.*?)</b>页"
            page = re.compile(pat3).findall(list_data)
            if(len(page) > 0):
                pass
            else:
                # 只有1页
                page = [1]
            all_page.append({k: page[0]})
            if(n > 1):
                break
            n += 1
        n = 0
        for p1 in cat_all_data:
            this_page = all_page[n][p1]
            for p2 in range(1, int(this_page) + 1):
                this_page_url = "https://list.jd.com/list.html?cat=" + str(p1) + "&page=" + str(p2)
                #print(this_page_url)
                yield Request(this_page_url, callback = self.parse)
            n += 1
    def parse(self, response):
        item = JdgoodsItem()
        list_data = response.body.decode("utf-8", "ignore")
        # 频道1,2
        pd = response.xpath("//span[@class='curr']/text()").extract()
        if(len(pd) == 0):
            pd = ["缺省", "缺省"]
        if(len(pd) == 1):
            pda = pd[0]
            pd = [pda, "缺省"]
        pd1 = pd[0]
        pd2 = pd[1]
        #print(pd1)
        # 图书名 (从下标3的地方开始获取)
        book_name = response.xpath("//div[@class='p-name']/a/em/text()").extract()
        #print(book_name)
        # 价格
        all_skupat = '<a data-sku="(.*?)"'
        all_sku = re.compile(all_skupat).findall(list_data)
        # 店家
        seller = response.xpath("//span[@class='curr-shop']/text()").extract()
        # 处理当前页数据
        for r in range(0, len(seller)):
            name = book_name[r + 3]
            this_sku = all_sku[r]
            price_url = "https://p.3.cn/prices/mgets?callback=jQuery5975516&type=1&skuIds=J_" + str(this_sku)
            # print(price_url)
            # 注: 访问频繁之后这里请求就会返回验证码了。。。
            price_data = urllib.request.urlopen(price_url).read().decode("utf-8", "ignore")
            price_pat = '"p":"(.*?)"'
            price = re.compile(price_pat).findall(price_data)[0]
           # print(name + ' -- ' + price)
            print(seller)
            item["sub1"] = pd1
            item["sub2"] = pd2
            item["seller"] = seller
            item["price"] = price
            item["name"] = name

            yield item
