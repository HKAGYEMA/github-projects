
#import scrapy 
#from parsel import Selector
#from scrapy.spiders import CrawlSpider, Rule
#from scrapy.linkextractors import LinkExtractor
import time
import requests
from bs4 import BeautifulSoup
start = time.time()
  
inverted_index = {}
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

    for link in all_links:
        if 'places/default/edit' not in link: #ignore edit pages
            print('scraping' + link)
            link_source = requests.get(base_path + link) .text
            link_soup = BeautifulSoup(link_source, 'lxml')
    for row in link_soup.find_all('td', class_ ='w2p_fw'):
        word = row.text.strip()
        if word is not '':

            if word not in inverted_index:
                inverted_index.update({word:{link:1}})
            elif link in inverted_index[word]:
                inverted_index[word][link] +=1
            else:
                inverted_index[word].update({link:1})

    for link in link_soup.find_all('a'):
        if 'places/default/user' not in link['href'] and link['href'] not in all_links:
            all_links.append(link['href'])
    time.sleep(5)
    #return inverted_index
 
