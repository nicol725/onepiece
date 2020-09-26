import scrapy


class CityspiderSpider(scrapy.Spider):
    name = 'cityspider'
    allowed_domains = ['lajifenleiapp.com']
    start_urls = ['http://lajifenleiapp.com/']

    def parse(self, response):

        pass
