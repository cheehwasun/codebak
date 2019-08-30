# -*- coding: utf-8 -*-
import scrapy


class SocceroddSpider(scrapy.Spider):
    name = 'soccerodd'
    allowed_domains = ['www.win007.com']
    start_urls = ['http://www.win007.com/']

    def parse(self, response):
        pass
