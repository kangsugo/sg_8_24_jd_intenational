# -*- coding: utf-8 -*-
import scrapy


class GoodsSpider(scrapy.Spider):
    name = "goods"
    allowed_domains = ["jd.hk"]
    start_urls = (
        'http://www.jd.hk/',
    )

    def parse(self, response):
        for line in open('diversity_url.txt'):
            token = line.split('@')
            url = token[1]
            name = token[2]
            new_url =  "https://"+url.replace("//","").strip()
            yield scrapy.Request(new_url,meta={'diversity':name},callback=self.get_goods)

    def get_goods(self,response):
        diver = response.meta['diversity']
        url = response.request.url
        page = response.xpath('//span[@class="p-skip"]/em/b/text()').extract()
        if page == [] :
            pass
        else:
            txt =  "  @ "+diver.replace("\n","").strip()+"  @ "+url.replace("\n","").strip()+"  @ "+page[0].encode('utf-8').replace("\n","").strip()
            with open('goods_page_num.txt','a') as ff:
                ff.write(txt+'\n')


            # ones = response.xpath('//li[@class="gl-item"]')
            # for one in ones:
            #     sku = one.xpath('@data-sku').extract()
            #     if sku == []:
            #         pass
            #     else:
            #         # print good
            #         print diver
            #         print sku[0].encode('utf-8')
            #         # print "https:"+url[0].encode('utf-8').strip()
            #         # print sku[0].encode('utf-8')
