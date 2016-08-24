# -*- coding: utf-8 -*-
import scrapy
import string
import db
from scrapy.selector import Selector

class GoodSpider(scrapy.Spider):
    name = "good"
    allowed_domains = ["jd.hk"]
    start_urls = (
        'http://www.jd.hk/',
    )
    def __init__(self):
        self.db = db.kang()


    def parse(self, response):
        f = open("F:\get_good_url\good_board_url.txt")
        for line in f:
            tokens =  line.split()
            # print tokens
            ur = tokens[1]
            name = tokens[0]

            # 具体的解析也需要分情况
            #url: https://search.jd.hk/Search?keyword=%E7%AB%A5%E8%A3%85&page=266
            if ur.find('list') == -1:
                yield scrapy.Request(ur,meta={"name":name},callback=self.list_notin_url)



            #2.url:https://list.jd.hk/list.html?cat=1319,1525,7057&page=1
            else:
                yield scrapy.Request(ur,meta={"name":name},callback=self.list_in_url)
        f.close()



    def list_in_url(self,response):
        div_name = response.meta['name']
        node = response.xpath('//li[@class="gl-item"]').extract()
        for one in node:
            s = Selector(text=one)
            name = s.xpath('//em/text()').extract()
            good_name =  name[0].encode('utf-8')
            sku = s.xpath('//a[@class="J_focus"]/@data-sku').extract()
            good_sku =  string.atoi(sku[0].encode('utf-8'))
            self.db.process_raw_world(good_sku,good_name,div_name)



    def list_notin_url(self,response):
        div_name = response.meta['name']
        node = response.xpath('//li[@class="gl-item"]').extract()
        for one in node:
            s = Selector(text=one)
            name = s.xpath('//div[@class="p-name"]/a/em/text()').extract()
            good_name =  name[0].encode('utf-8')
            sku = s.xpath('//div[@class="p-operate"]/a/@skuid').extract()
            good_sku =  string.atoi(sku[0].encode('utf-8'))
            self.db.process_raw_world(good_sku, good_name, div_name)



    def __del__(self):
        self.db.destr()