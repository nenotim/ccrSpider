# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CCopyRightItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    number = scrapy.Field()
    type = scrapy.Field()
    name = scrapy.Field()
    shortName = scrapy.Field()
    version = scrapy.Field()
    company = scrapy.Field()
    publishDate = scrapy.Field()
    registerDate = scrapy.Field()
    pass
