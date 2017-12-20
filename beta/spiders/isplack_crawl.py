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
        stars = []
        recent_rev = response.xpath('//div[@id="most-recent-reviews-content"]/div[@class="a-section review"]/div[@class="a-icon-row a-spacing-none"]/a/i/span/text()').extract()
        for i in recent_rev:
             i = i.split(' ')
             i = i[0]
             stars.append(i)
        reviews = response.xpath('//div[@id="most-recent-reviews-content"]/div[@class="a-section review"]/a/span/text()').extract()
        #reviews = recent_rev.xpath('//span[@class="a-icon-alt"]').extract()
        #/div[@class="a-profile-content"]/span[@class="a-profile-name"]/text()').extract()
        #reviews = recent_rev.xpath('/').extract()
        rank = response.xpath('//li[@id="SalesRank"]').extract_first().replace('\n','').replace('<b>','').replace('</b>','').split('(')[0].replace('<li id="SalesRank">','')

        yield {
            'titled': title,
            'stars': stars,
            'rank': rank,
            'rec_rev-1': reviews[0],
            'rec_rev-2': reviews[1],
            'rec_rev-3': reviews[2],
            'rec_rev-4': reviews[3],
            'rec_rev-5': reviews[4],
            'rec_rev-6': reviews[5],
            'rec_rev-7': reviews[6],
            'rec_rev-8': reviews[7],
            'rec_rev-9': reviews[8],
            'rec_rev-10': reviews[9] 
        }
