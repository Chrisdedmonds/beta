# -*- coding: utf-8 -*-
import scrapy
import datetime


class IsplackCrawlSpider(scrapy.Spider):
    name = 'isplack-crawl'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/gp/product/B00M7QSHE6?m=15827540011/']

    def start_requests(self):
        for i in self.start_urls:
            yield scrapy.Request(i, callback=self.parse, headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'})

    def parse(self, response):
        a = response.text
        title = response.xpath('//title/text()').extract_first()
        title = title.split(':')
        title = title[1]
        name = 'isplack'
        date = str(datetime.date.today())
        '''
        with open( 'repo/' + name + '_' + date + '.html', 'w') as fil:
            fil.write(a)
        fil.close()
        '''
        yield {
            'title': title
        }
