import json

import scrapy
import requests

from ..items import LagouItem

#拉钩网中的数据和页面是分开获取的，所以我们目标是获取核心数据的json
#当我们随便进入拉钩的网站的任意一个页面时，拉钩会自动为我们这台电脑分配cookie
#核心请求https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false
#403:检查头部信息不够（浏览器版本），cookies（瞬时的，不能太久）
#对策 ：需要每一次访问ajax请求之前，先去访问页面，为了得到全新的获取cookie
# 主网页：https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=

class LagouspiderSpider(scrapy.Spider):
    name = 'lagouspider'
    allowed_domains = ['lagou.com']
    # start_urls = ['http://lagou.com/']
    headers={
        'user-agent':'Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/79.0.3945.79Safari/537.36',

        # #https
        'referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'accept':'application/json,text/javascript,*/*;q=0.01',
        # 'accept': 'application/json,text/javascript,*/*;q=0.01',
        # 'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        # 'user-agent': 'Mozilla/5.0(Windows NT 6.3;WOW64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/78.0.3904.108Safari/537.36'
    }
    cookies_msg=""
    url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
    # first = "true"
    pn=1
    # kd="python"

    #在scrapy发送请求之前，先为request对象初始化
    def start_requests(self):
        main_url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
        cookies = requests.get(main_url,headers=self.headers).cookies
        # print(requests.get(main_url, headers=self.headers).cookies)
        #将获取到的cookie对象变为字典
        self.cookies_msg =requests.utils.dict_from_cookiejar(cookies)
        # time.sleep(0.5)触发时间戳  访问太频繁
        yield scrapy.FormRequest(url=self.url,formdata={'first':"true",'pn':str(self.pn),'kd':"python"},callback=self.parse,headers=self.headers,cookies=self.cookies_msg)

    def parse(self, response):
        data = json.loads(response.body, encoding='utf-8')
        #拿到岗位的整体数据
        work_msg = data['content']['positionResult']['result']
        for wm in work_msg:
            print(wm['positionName'])
            work = LagouItem()
            work['work_name'] = wm['positionName']
            work['company'] = wm['companyFullName']
            work['salary'] = wm['salary']
            work['work_year'] = wm['workYear']
            work['education'] = wm['education']
            work['city'] = wm['city']
            work['district'] = wm['district']
            yield work
        if self.pn <= 9:
            self.pn += 1
            yield scrapy.FormRequest(url=self.url,formdata={'first':'true','pn':str(self.pn),'kd':"python"},callback=self.parse,headers=self.headers,cookies=self.cookies_msg)
        pass
