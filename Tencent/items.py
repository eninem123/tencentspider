# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    name_link = scrapy.Field()
    type = scrapy.Field()
    num = scrapy.Field()
    location = scrapy.Field()
    times = scrapy.Field()




class PosiItem(scrapy.Item):
    zhize = scrapy.Field()
    yaoqiu = scrapy.Field()