# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import openpyxl
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WeiboscrapyPipeline:
    def __init__(self):
        self.count = 0
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.title = 'data'
        self.ws.append(('time', 'text'))

    def close_spider(self, spider):
        self.wb.save('weibo1.xlsx')

    def process_item(self, item, spider):
        self.count = self.count + 1
        line = [item['time'], item['text']]
        # print(line)
        self.ws.append(line)
        if self.count % 100 == 0:
            self.wb.save('weibo1.xlsx')
            print("成功写入100条数据")
        return item
