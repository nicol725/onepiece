import scrapy
import time

from ..items import RubbishItem


class RubbishspiderSpider(scrapy.Spider):
    name = 'rubbishSpider'
    allowed_domains = ['lajifenleiapp.com']
    start_urls = ['http://lajifenleiapp.com/']

    def parse(self, response):
        # scrapy.Request(url=self.url,dont_filter=True)
        current_item = response.xpath('//div[@class="row"]/div[@class="col-md-12 col-xs-12 city_list"]/a')
        for it in current_item:
            rb = RubbishItem()
            rb['city'] = it.xpath('text()').extract()[0]
            url = str(self.start_urls[0])+it.xpath('@href').extract()[0]
            # yield rb
            time.sleep(0.1)
            yield scrapy.Request(url, meta={'item': rb}, callback=self.parse_msg,dont_filter=True)  # dont_filter不用过滤二级页面
        pass

    def parse_msg(self,response):
        rb =response.meta['item']
        rb['kind1'] = response.xpath('//div[1]/div[16]/div/div[2]/div[1]/div/div[2]/h3/text()').extract()
        rb['kind1_note'] = response.xpath('//div[1]/div[16]/div/div[2]/div[1]/div/div[2]/p/text()').extract()
        rb['kind2'] = response.xpath('//div[1]/div[16]/div/div[2]/div[2]/div/div[2]/h3/text()').extract()
        rb['kind2_note'] = response.xpath('//div[1]/div[16]/div/div[2]/div[2]/div/div[2]/p/text()').extract()
        rb['kind3'] = response.xpath('//div[1]/div[16]/div/div[3]/div[1]/div/div[2]/h3/text()').extract()
        rb['kind3_note'] = response.xpath('//div[1]/div[16]/div/div[3]/div[1]/div/div[2]/p/text()').extract()
        rb['kind4'] = response.xpath('//div[1]/div[16]/div/div[3]/div[2]/div/div[2]/h3/text()').extract()
        rb['kind4_note'] = response.xpath('//div[1]/div[16]/div/div[3]/div[2]/div/div[2]/p/text()').extract()
        rb['kind5'] = response.xpath('//div[1]/div[17]/div/div[4]/div/div/div[2]/h3/text()').extract()
        rb['kind5_note'] = response.xpath('//div[1]/div[17]/div/div[4]/div/div/div[2]/p/text()').extract()
        if not rb['kind1']:
            rb['kind1'] = response.xpath('//div[1]/div[17]/div/div[2]/div[1]/div/div[2]/h3/text()').extract()[0]
            rb['kind1_note'] = response.xpath('//div[1]/div[17]/div/div[2]/div[1]/div/div[2]/p/text()').extract()[0]
        else:
            rb['kind1'] = rb['kind1'][0]
            rb['kind1_note'] = rb['kind1_note'][0]
        if not rb['kind2']:
            rb['kind2'] = response.xpath('//div[1]/div[17]/div/div[2]/div[2]/div/div[2]/h3/text()').extract()[0]
            rb['kind2_note'] = response.xpath('//div[1]/div[17]/div/div[2]/div[2]/div/div[2]/p/text()').extract()[0]
        else:
            rb['kind2'] = rb['kind2'][0]
            rb['kind2_note'] = rb['kind2_note'][0]
        if not rb['kind3']:
            rb['kind3'] = response.xpath('//div[1]/div[17]/div/div[3]/div[1]/div/div[2]/h3/text()').extract()[0]
            rb['kind3_note'] = response.xpath('//div[1]/div[17]/div/div[3]/div[1]/div/div[2]/p/text()').extract()[0]
        else:
            rb['kind3'] = rb['kind3'][0]
            rb['kind3_note'] = rb['kind3_note'][0]
        if not rb['kind4']:
            rb['kind4'] = response.xpath('//div[1]/div[17]/div/div[3]/div[2]/div/div[2]/h3/text()').extract()[0]
            rb['kind4_note'] = response.xpath('//div[1]/div[17]/div/div[3]/div[2]/div/div[2]/p/text()').extract()[0]
        else:
            rb['kind4'] = rb['kind4'][0]
            rb['kind4_note'] = rb['kind4_note'][0]
        if not rb['kind5']:
            rb['kind5'] = "敬请期待"
            rb['kind5_note'] = "敬请期待"
        else:
            rb['kind5'] = rb['kind5'][0]
            rb['kind5_note'] = rb['kind5_note'][0]
        yield rb
        pass