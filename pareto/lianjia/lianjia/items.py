# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianJiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    total_price = scrapy.Field()
    unit_price = scrapy.Field()
    pass
