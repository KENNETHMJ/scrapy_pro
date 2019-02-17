# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery
from ..items import City58Item

class SpiderCity58Spider(scrapy.Spider):
    name = 'spider_city_58'
    allowed_domains = ['58.com']
    start_urls = ['http://gz.58.com/chuzu/']

    def parse(self, response):
        jpy = PyQuery(response.text)
        li_list = jpy('body > div.mainbox > div > div.content > div.listBox > ul > li').items()
        for it in li_list:
            a_tag = it('div.des > h2 > a')
            item = City58Item()
            item['name'] = a_tag.text()
            item['url'] = a_tag.attr('href')
            item['price'] = it('div.listliright > div.money > b').text()
            yield item
        # print('Ken in phase')
