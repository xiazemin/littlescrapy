# coding=utf8

import scrapy
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class DmozSpider(scrapy.Spider):
    name = "dmoz33"
    allowed_domains = ["douban.com"]

    start_urls = [
        "https://movie.douban.com/top250",
        "https://movie.douban.com/chart"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        # open(filename, 'wb').write(response.body)
        # filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            print 'CCCCCCCC'
            f.write(response.body)
