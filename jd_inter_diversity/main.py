#coding:utf-8
# from selenium  import webdriver
from selenium  import webdriver
import HTMLParser
from scrapy.selector import Selector
driver = webdriver.Firefox()
driver.get('https://www.jd.hk/')

# 获取执行后的页面，针对不需要用户干预的情况
# time.sleep(30)

# name =driver.find_element_by_xpath('/html')
name = driver.page_source
html_parser = HTMLParser.HTMLParser()
txt = html_parser.unescape(name)  # 这样就得到了txt = '<abc>'
# print txt


content = Selector(text=name)
print content
tag = content.xpath('//div[@class="sub-menu"]/div[@class="sub-list"]/ul/li')
print tag
for one in tag:
    ur = one.xpath('a/@href').extract()
    tag = one.xpath('a/text()').extract()
    print ur[0]
    print type(str(ur[0]))
    print tag[0].encode('utf-8')
    print type(tag[0].encode('utf-8'))
    insert = "@  "+str(ur[0]) +"   @  " + tag[0].encode('utf-8') + "\n"
    with open("id.txt","a") as ff:
        ff.write(insert)
driver.close()