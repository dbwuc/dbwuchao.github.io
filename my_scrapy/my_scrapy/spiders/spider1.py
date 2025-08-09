import scrapy


class Spider1Spider(scrapy.Spider):
    name = 'spider1'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
