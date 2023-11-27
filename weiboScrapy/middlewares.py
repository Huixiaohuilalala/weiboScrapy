# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

def get_cookies_dict():
    cookies_str = 'SINAGLOBAL=4202245085929.3926.1694075023160; UOR=,,www.google.com; ALF=1703150770; SCF=Ag_in7mgRA_uN0HjoLgRcgQk8YwMOZZKCjXt4f-LTmoHy1PWPkXLujxOJ4OvoCXtw_2frYcEaJxXpZwwePMkaHQ.; _s_tentry=weibo.com; Apache=3394088968541.0757.1700983329843; ULV=1700983329847:22:12:2:3394088968541.0757.1700983329843:1700971384306; WBtopGlobal_register_version=2023112621; PC_TOKEN=df520c5071; crossidccode=CODE-yf-1R7f0I-1WwMJE-KKQSyN6cuOMQBt6a13f04; SSOLoginState=1701004642; SUB=_2A25IZzUyDeRhGeBO6lEY8C7JyzSIHXVrHcj6rDV8PUJbkNANLUjEkW1NSjFAl32PuSutK5_BST2lmIEFDem2MSof; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWvKUwArb5uQNpFnJ3bogTR5NHD95Qceh201K57SK5RWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNSo5pe0.7eh-715tt'
    cookies_dict = {}
    for item in cookies_str.split('; '):
        key, value = item.split('=', maxsplit=1)
        cookies_dict[key] = value
    return cookies_dict


COOKIES_DICT = get_cookies_dict()

class WeiboscrapySpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class WeiboscrapyDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        request.cookies = COOKIES_DICT
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
