# -*- coding: utf-8 -*-
import scrapy


class IsplackCrawlSpider(scrapy.Spider):
    name = 'isplack-crawl'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    def parse(self, response):
        pass
