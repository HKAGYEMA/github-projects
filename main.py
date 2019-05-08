
import requests
from parsel import Selector
import scrapy
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

#class PagesSpider(CrawlSpider):
    #name = "pages"
    #allowed_domains = ['http://example.webscraping.com']
    #base_path = ['http://example.webscraping.com']

    #rules = (
        #Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
             #callback="parse_item",
             #follow=True),)

#def parse_item(self, response):
    #all_links = response.css(' .large > .detailslisk::attr(href)') .extract()
    #for a in all_links:
        #yield scrapy.Request(a, callback=self.parse)
    #print('Processing..' + response.url)

#def parse(self, response):

    #title = response.css('title::text') .extract_first()
            #get anchor tags
    #links = response.css('a::attr(href)') .extract()

  
  
class ExtractUrls(scrapy.Spider): 
    name = "extract"
  
    # request function 
def start_requests(self): 
        urls = [ 'http://example.webscraping.com', ] 
          
        for url in urls: 
            yield scrapy.Request(url = url, callback = self.parse) 
  
    # Parse function 
def parse(self, response): 
          
        # Extra feature to get title 
        title = response.css('title::text').extract_first()  
          
        # Get anchor tags 
        links = response.css('a::attr(href)').extract()      
          
        for link in links: 
            yield 
            { 
                'title': title, 
                'links': link 
            } 
              
            if 'webcrawler' in link:          
                yield scrapy.Request(url = link, callback = self.parse)
