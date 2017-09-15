# coding=utf8
import scrapy
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider,Rule



# class MukelistSpider(scrapy.Spider):
#
#     name = "doubanmoive"
#     allowed_domains = ["movie.douban.com"]
#     start_urls = ["http://movie.douban.com/top250"]
#
#     rules = [
#         Rule(SgmlLinkExtractor(allow=(r'http://movie.douban.com/top250\?start=\d+.*'))),
#         Rule(SgmlLinkExtractor(allow=(r'http://movie.douban.com/subject/\d+')), callback="parse_item"),
#     ]
#
#     def parse_item(self, response):
#         sel = Selector(response)
#         item = DoubanmoiveItem()
#         item['name'] = sel.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
#         item['year'] = sel.xpath('//*[@id="content"]/h1/span[2]/text()').re(r'\((\d+)\)')
#         item['score'] = sel.xpath('//*[@id="interest_sectl"]/div/p[1]/strong/text()').extract()
#         item['director'] = sel.xpath('//*[@id="info"]/span[1]/a/text()').extract()
#         item['classification'] = sel.xpath('//span[@property="v:genre"]/text()').extract()
#         item['actor'] = sel.xpath('//*[@id="info"]/span[3]/a[1]/text()').extract()
#         return item





# class DoubanmoiveItem(Item):
#     name=Field()#电影名
#     year=Field()#上映年份
#     score=Field()#豆瓣分数
#     director=Field()#导演
#     classification=Field()#分类
#     actor=Field()#演员