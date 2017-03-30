# -*- coding: utf-8 -*-
# Script Name	: dd.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-03-19
# Description	: Scrapy实现当当网商品爬虫实战


import scrapy
from dangdang.items import DangdangItem
from scrapy.http import Request

class DdSpider(scrapy.Spider):
    name = "dd"
    allowed_domains = ["dangdang.com"]
    start_urls = ['http://category.dangdang.com/pg1-cid4008154.html']

    def parse(self, response):
        for i in range(1, 3):
            url = "http://category.dangdang.com/pg" + str(i) + "-cid4008154.html"
            yield Request(url, callback = self.handle_items)
    def handle_items(self, response):
        item = DangdangItem()
        item["title"] = response.xpath("//a[@name='sort-big-pic']/@title").extract()
        item["link"] = response.xpath("//a[@name='sort-big-pic']/@href").extract()
        item["comment"] = response.xpath("//a[@name='sort-evaluate']/text()").extract()
        yield item
