# coding=utf8

import scrapy
import re

# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
'''
豆瓣读书评分9分以上榜单

'''


class bookshow(scrapy.Spider):
    name = "douban_bookshow"
    allowed_domains = ["douban.com"]

    start_urls = [
        "https://www.douban.com/doulist/1264675/"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # open(filename, 'wb').write(response.body)
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     print 'CCCCCCCCCCCCCCCC'
        #     f.write(response.body)
        selector = scrapy.Selector(response)
        books = selector.xpath('//div[@class="bd doulist-subject"]')
        filename = 'aa.txt'
        files = open(filename, 'ab+')

        print 'AAAAAAAAAA:', len(books)

        files.write(len(books))

        for ii in range(1, 20):
            files.write(ii)
        print 'hah'
        files.flush()
        files.close()
        # for each in books:
        #     files.write(each)
            # title = each.xpath('div[@class="title"]/a/text()').extract()[0]
            # rate = each.xpath('div[@class="rating"]/span[@class="rating_nums"]/text()').extract()[0]
            # author = re.search('<div class="abstract">(.*?)<br', each.extract(), re.S).group(1)
            # print '标题:' + title
            # print '评分:' + rate
            # print author
            # print ''
