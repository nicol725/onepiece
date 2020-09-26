# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    post = scrapy.Field()#职位名
    company = scrapy.Field()#公司名
    position = scrapy.Field()#工作地点
    salary = scrapy.Field()#薪资
    time = scrapy.Field()#发布时间
    method = scrapy.Field()#智能要求
    pass
