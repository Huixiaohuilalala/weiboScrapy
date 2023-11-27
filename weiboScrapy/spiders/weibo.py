import scrapy
from scrapy import Request
import datetime

from weiboScrapy.items import WeiboscrapyItem


class WeiboSpider(scrapy.Spider):
    name = "weibo"
    allowed_domains = ["s.weibo.com"]

    def start_requests(self):
        baseUrl = "https://s.weibo.com/weibo?q=巴以冲突&typeall=1&suball=1&timescope=custom%3A"
        month = 10
        day = 7
        while day < 32:
            start_time = datetime.datetime(year=2023, month=month, day=day, hour=0)
            if month == 10 and day == 31:
                end_time = datetime.datetime(year=2023, month=12, day=1, hour=0)
            else:
                end_time = datetime.datetime(year=2023, month=month, day=day + 1, hour=0)
            print(f"开始爬取{month}月{day}日数据")
            for page in range(15):
                _start_time = start_time.strftime("%Y-%m-%d-%H")
                _end_time = end_time.strftime("%Y-%m-%d-%H")
                url = baseUrl + str(_start_time) + "%3A" + str(_end_time) + "&Refer=g&page=" + str(page)
                yield Request(url=url)
            day = day + 1
        month = 11
        day = 1
        while day < 27:
            start_time = datetime.datetime(year=2023, month=month, day=day, hour=0)
            end_time = datetime.datetime(year=2023, month=month, day=day + 1, hour=0)
            print(f"开始爬取{month}月{day}日数据")
            for page in range(15):
                _start_time = start_time.strftime("%Y-%m-%d-%H")
                _end_time = end_time.strftime("%Y-%m-%d-%H")
                url = baseUrl + str(_start_time) + "%3A" + str(_end_time) + "&Refer=g&page=" + str(page)
                yield Request(url=url)
            day = day + 1

    def parse(self, response):
        # items = response.xpath('//div[@class="card-wrap"]//div[@class="content"]')
        list_items = response.xpath('//div[@class="card-wrap"]//div[@class="content"]/p[last()]')
        time_items = response.xpath('//div[@class="content"]/div[@class="from"]/a[1]/text()').extract()
        n = len(list_items)
        for i in range(n):
            texts = list_items[i].xpath('text()').extract()
            finaltext = ''.join(texts)
            item = WeiboscrapyItem()
            item['text'] = finaltext
            time = time_items[i].strip()
            time = time[0:6]
            # print(time)
            item['time'] = time
            yield item
