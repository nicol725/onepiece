# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
#解析并获取内容数据
import sys

import importlib#sys版本问题解决
default_encoding = 'utf-8'

if sys.getdefaultencoding() != default_encoding:#判断系统当前默认字符是否为utf-8
    importlib.reload(sys)
    # reload(sys)#使用reload()函数重新加载sys模块
    # (default_encoding)#设置系统默认字符集为utf-8sys.setdefaultencoding

import xlwt
#输出到表格
class DoubanmoviePipeline:
    def process_item(self, item, spider):#输出显示 item就是传递过来的每一个对象
        print("排名TOP："+ item['rank'][0])
        print("电影名称："+item['title'][0])
        print("详情链接：" + item['link'][0])
        print("豆瓣评分：" + item['rating'][0]+'('+item['participants'][0]+')')
        print("最新评论：" + item['quote'][0])
        return item
