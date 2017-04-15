# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdgoodsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 频道1, 2
    sub1 = scrapy.Field()

    sub2 = scrapy.Field()
    # 图书名
    name = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 店家
    seller = scrapy.Field()
