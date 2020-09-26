# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import urllib.request

from itemadapter import ItemAdapter
#解析并获取内容数据
import sys

import importlib#sys版本问题解决
default_encoding = 'utf-8'

if sys.getdefaultencoding() != default_encoding:#判断系统当前默认字符是否为utf-8
    importlib.reload(sys)
    # reload(sys)#使用reload()函数重新加载sys模块
    # (default_encoding)#设置系统默认字符集为utf-8sys.setdefaultencoding

from openpyxl import Workbook

class DoubanmoviePipeline:

    def process_item(self, item, spider):#输出显示 item就是传递过来的每一个对象
        print("排名TOP："+ item['rank'][0])
        print("电影名称："+item['title'][0])
        print("详情链接：" + item['link'][0])
        print("豆瓣评分：" + item['rating'][0]+'('+item['participants'][0]+')')
        print("最新评论：" + item['quote'][0])
        print("图片："+item['pic'][0])

        #利用openpyxl存入表格
        # def __init__(self):
        #     self.wb = Workbook()
        #     self.ws = self.wb.active
        #     self.ws.append(['排名top', '电影名称', '详情链接', '豆瓣评分', '参评人数', '最新评论'])
        # line=[
        #     item['rank'][0],
        #     item['title'][0],
        #     item['link'][0],
        #     item['rating'][0],
        #     item['participants'][0],
        #     item['quote'][0],
        # ]
        # self.ws.append(line)
        # self.wb.save('TOP250.xls')

        urllib.request.urlretrieve(item['pic'][0],"D:\images/{}.jpg".format(item['title'][0]))
        return item


