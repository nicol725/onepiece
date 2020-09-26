# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from mysite.models import Movie
class DoubanItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = Movie#让当前类和django中创建的模板类互通
    pass
