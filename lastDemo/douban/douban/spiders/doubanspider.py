import scrapy
from ..items import DoubanItem

class DoubanspiderSpider(scrapy.Spider):
    name = 'doubanspider'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']  # 列表类型指定需要爬取的网页，如果有多个可以追加列表元素','分隔

    # 爬虫主程序会自动运行，主要用于解析页面数据
    def parse(self, response):  # response代表程序获取网页的代码，也就是我们需要解析的代码内容
        # 获取当前页面中的电影信息标签<div class="item">并生成一个列表

        # //相对路径
        currentpage_movie_items = response.xpath('//div[@class="item"]')
        # 循环遍历电影信息列表
        for movie_item in currentpage_movie_items:  # 单个页面的数据
            # 获取采集数据并且复制DoubanmovieItem类成员
            # 创建一个Movie对象
            movie = DoubanItem()
            # xpath下标从1开始
            movie['rank'] = movie_item.xpath('div[@class="pic"]/em/text()').extract()[0]  # extract返回一个list
            movie['title'] = movie_item.xpath(
                'div[@class="info"]/div[@class="hd"]/a/span[@class="title"][1]/text()').extract()[0]
            movie['link'] = movie_item.xpath('div[@class="pic"]/a/@href').extract()[0]
            movie['rating'] = movie_item.xpath(
                'div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            movie['participants'] = movie_item.xpath(
                'div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[last()]/text()').extract()[0]
            movie['quote'] = movie_item.xpath(
                'div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()').extract()[0]

            if not movie['quote']:
                movie['quote']="有待评论"
            # movie['pic'] = movie_item.xpath('div[@class="pic"]/a/img/@src').extract()
            # 将封装好的一个电影信息添加到容器中，yield作用是创建一个列表并添加元素
            yield movie  # 创建一个序列
        pass
        # 请求下一页数据
        next_page = response.xpath("//span[@class='next']/a/@href")
        if next_page:  # 最后一页没有下一页数据，判断是否有下一页
            url = response.urljoin(next_page[0].extract())  # 下一页地址
            # yield scrapy.Request(url,self.parse,headers=self.headers)#递归请求,携带头部信息
            yield scrapy.Request(url, self.parse)  # 递归请求,携带头部信息



