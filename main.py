
import requests
from parsel import Selector
#import openpyxl as op
#import pandas as pd
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import time
start = time.time()


all_links = []
base_path = 'http://example.webscraping.com'
response = requests.get(base_path)
selector = Selector(response.text)
href_links = selector.xpath('//a/@href').getall()
all_links += href_links

sheet_name = "URLs"

for link in href_links:
    try:
        response = requests.get(base_path + link)
        selector = Selector(response.text)
        href_links_2 = selector.xpath('//a/@href').getall()
        all_links += href_links_2
        if len(all_links) >=10:
            break
    except Exception as exp:
                print('Error navigating to link : ', link)
                print(all_links)
                end = time.time()
                print("Time taken in seconds : ", (end-start))

class PagesSpider(CrawlSpider):
    name = "pages"
    allowed_domains = ['http://example.webscraping.com']
    base_path = ['http://example.webscraping.com']

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        print('Processing..' + response.url)
