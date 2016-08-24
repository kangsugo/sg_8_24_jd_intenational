import random
import base64
import json


# from settings import PROXIES


class RandomUserAgent(object):
    """Randomly rotate user agents based on a list of predefined ones"""  #

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        print "**************************" + random.choice(self.agents)
        request.headers.setdefault('User-Agent', random.choice(self.agents))


# class ProxyMiddleware(object):
#     def process_request(self, request, spider):
#
#         PROXIES = [
#             {"ip_port": "111.155.116.237:8123", "user_pass": ""}, {"ip_port": "120.15.168.146:8118", "user_pass": ""},
#             {"ip_port": "120.25.171.183:8080", "user_pass": ""}, {"ip_port": "60.13.74.187:843", "user_pass": ""},
#             {"ip_port": "183.61.236.54:3128", "user_pass": ""}, {"ip_port": "101.201.235.141:8000", "user_pass": ""},
#             {"ip_port": "101.231.250.102:80", "user_pass": ""}, {"ip_port": "119.53.124.91:8118", "user_pass": ""},
#             {"ip_port": "122.190.229.20:8118", "user_pass": ""}, {"ip_port": "114.33.202.73:8118", "user_pass": ""},
#             {"ip_port": "171.38.182.37:8123", "user_pass": ""}, {"ip_port": "220.166.242.152:8118", "user_pass": ""},
#             {"ip_port": "123.57.52.171:80", "user_pass": ""}, {"ip_port": "115.160.137.178:8088", "user_pass": ""},
#             {"ip_port": "171.39.234.9:80", "user_pass": ""}, {"ip_port": "222.42.230.76:80", "user_pass": ""},
#             {"ip_port": "123.134.196.78:80", "user_pass": ""}, {"ip_port": "111.201.197.141:8118", "user_pass": ""},
#             {"ip_port": "202.107.92.213:80", "user_pass": ""}
#         ]
#
#         f = open('my_ippool.json')
#         PROXIES = json.load(f)
#         proxy = random.choice(PROXIES)
#         if proxy['user_pass'] is not None:
#             request.meta['proxy'] = "http://%s" % proxy['ip_port']
#             encoded_user_pass = base64.encodestring(proxy['user_pass'])
#             request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
#             print "**************ProxyMiddleware have pass************" + proxy['ip_port']
#         else:
#             print "**************ProxyMiddleware no pass************" + proxy['ip_port']
#             request.meta['proxy'] = "http://%s" % proxy['ip_port']
#
# # *****************************
#
# # import os
# # import random
# # from scrapy.conf import settings
# # class RandomUserAgentMiddleware(object):
# #    def process_request(self, request, spider):
# #        ua  = random.choice(settings.get('USER_AGENT_LIST'))
# #        if ua:
# #            request.headers.setdefault('User-Agent', ua)
#
# # class ProxyMiddleware(object):
# #    def process_request(self, request, spider):
# #        request.meta['proxy'] = settings.get('HTTP_PROXY')
