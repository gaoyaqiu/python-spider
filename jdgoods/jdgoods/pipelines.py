# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class JdgoodsPipeline(object):

    def __init__(self):
        self.conn = pymysql.connect(host = "127.0.0.1", user = "root", password = "ok", db = "jdgoods")

    def process_item(self, item, spider):

        try:
            name = item["name"]
            price = item["price"]
            seller = item["seller"]
            sub1 = item["sub1"]
            sub2 = item["sub2"]

            sql = "insert into goods (name, sub1, sub2, seller, price) values('" + name + "', '" + sub1 + "', '" + sub2 + "', '" + seller + "', '" + price + "')"
            self.conn.query(sql)

            return item
        except Exception as e:
            pass

    def close_spider(self):
        self.conn.close()


