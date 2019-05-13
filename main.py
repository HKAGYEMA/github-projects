
from selenium import webdriver 
import scrapy 
from parsel import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import time
import requests
from bs4 import BeautifulSoup
start = time.time()
import json
  

def getAndParseURL(result):
    #result = requests.get(url)
    soup = BeautifulSoup(result, 'html.parser')
    
    child = soup.find_all('a')
    for i in range(0, len(child)):
        if 'Next' in child[i].get_text():
            nextlink = child[i]['href']
            print(nextlink)
            return(nextlink)
    return None
    diction = {'location': "www.page.com/1", 'freq': "0"}
    r = requests.get("http://example.webscraping.com/places/default/view/Aland-Islands-2") 
    soup = BeautifulSoup(r, 'html.parser')
    
    child = soup.find_all('a')
    for i in range(0, len(child)):
        if 'Next' in child[i].get_text():
            nextlink = child[i]['href']
            print(nextlink)
            return(nextlink)
    return None

all_links = []
base_path = 'http://example.webscraping.com'
response = requests.get(base_path)
selector = Selector(response.text)
href_links = selector.xpath('//a/@href').getall()
all_links += href_links
# get URL 
r = requests.get("http://example.webscraping.com/") 
next = ''
#data = r.text 
#soup = BeautifulSoup(data) 
#table =  soup.findAll('td')
while(1):
    r = requests.get("http://example.webscraping.com/"+next) 

    data = r.text 
    soup = BeautifulSoup(data) 
    for link in soup.find_all('td'): 
        print(link.find('a')['href'])
    next = getAndParseURL(r.text)
    if next == None:
        break
    time.sleep(1)

    string = []
    for i in string:
        if i in diction:
            diction[i]['location'] = url 
            diction[i]['freq'] += 1
        else:
                userin = input().split()
        if userin[0] == ('print'):
                    printterm = userin[1]
    



