# -*- coding: utf-8 -*-
import scrapy
import urllib
from scrapy import FormRequest
import pymysql
import json
import random
from baidufanyi.items import BaidufanyiItem
from baidufanyi import settings
from scrapy_splash import SplashRequest
class FanyiSpider(scrapy.Spider):
    name = 'fanyi'
    #allowed_domains = ['sss']
    start_urls = ['https://fanyi.baidu.com/basetrans']
    headers = settings.HEADERS
    filepath = settings.FILEPATH

    def start_requests(self):
        with open(self.filepath,'r') as f:
            kws = f.readlines()
            for kw in kws:
                keyword = kw.strip()
                formdata = {
                    'query':  keyword,
                    'from':  'zh',
                    'to':  'en',
                }
                yield FormRequest(self.start_urls[0], formdata=formdata, callback=self.parse, headers=self.headers, dont_filter=True)

    def parse(self, response):
        item = BaidufanyiItem()
        item['origin'] = json.loads(response.text)['trans'][0]['dst']
        item['translation'] = json.loads(response.text)['trans'][0]['src']
        yield item
