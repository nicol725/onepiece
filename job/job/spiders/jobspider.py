import scrapy

import importlib#sys版本问题解决

import sys

from job.items import JobItem

default_encoding = 'utf-8'

if sys.getdefaultencoding() != default_encoding:#判断系统当前默认字符是否为utf-8
    importlib.reload(sys)

class JobspiderSpider(scrapy.Spider):
    name = 'jobspider'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    def parse(self, response):
        page_items = response.xpath('//div[@class="el"]')
        for job_item in page_items:
            job = JobItem()
            # job['post'] = job_item.xpath('normalize-space(//p/span/a)').extract()
            job['post'] = job_item.xpath('p/span/a/@title').extract()
            job['company'] = job_item.xpath('span[@class="t2"]/a/text()').extract()
            job['position'] = job_item.xpath('span[@class="t3"]/text()').extract()
            job['salary'] = job_item.xpath('span[@class="t4"]/text()').extract()
            job['time'] = job_item.xpath('span[@class="t5"]/text()').extract()
            if not job['salary']:
                job['salary'] = "商议决定"
            url = job_item.xpath('p/span/a/@href').extract()
            if url:
                #二级页面
                yield scrapy.Request(url[0],meta={'item':job},callback=self.parse_msg,dont_filter=True)#dont_filter不用过滤二级页面

        pass

    def parse_msg(self,response):
        job = response.meta['item']
        method=response.xpath('//div[@class="bmsg job_msg inbox"]/p/text()').extract()
        # print(method)
        job['method'] = method
        # for item in method:
        #     # print(item)
        #     job['method'] += item
        if job['post']:
            yield job
        pass
