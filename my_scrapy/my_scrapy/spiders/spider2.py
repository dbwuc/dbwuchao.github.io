import scrapy


class Spider2Spider(scrapy.Spider):
    name = 'spider2'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
