from bs4 import BeautifulSoup
from selenium import webdriver 
import scrapy 
from parsel import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import time
start = time.time()
import requests 



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
  
def country_data(string):
  page = requests.get(string)
  soup = BeautifulSoup(page.text, 'html.parser')
  site = ""
  results = soup.find_all('tr')
  i = 0
  for result in results:
    table_data = result.findAll('td')
    soup2 = BeautifulSoup(table_data[1].text, 'html.parser')
    if len(soup2.get_text().replace(" ","")) == 0:
      continue
    site += " "+soup2.get_text()
    i = 1+i
    print("",soup2.get_text(),"")
  ### Remove empty things and sort them
  sortSite = site.split(" ")
  for i in range(0, len(sortSite)-1):
    if sortSite[i] == '':
      sortSite.pop(i)
  sortSite.sort()
  return sortSite

print(country_data('http://example.webscraping.com/places/default/view/Afghanistan-1'))
