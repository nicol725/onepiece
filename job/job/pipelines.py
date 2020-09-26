# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class JobPipeline:
    def process_item(self, item, spider):
        print("职位："+item['post'][0])
        print("公司："+item['company'][0])
        print("位置："+item['position'][0])
        print("薪资："+item['salary'][0])
        print("发布时间："+item['time'][0])
        # print("任职需求："+item['method'][0])
        return item
