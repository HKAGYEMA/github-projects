from bs4 import BeautifulSoup
from selenium import webdriver 
import scrapy 
from parsel import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import time
start = time.time()
  
# importing requests 
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
  

for i in page_key:
    if i in words:
        foo = words[i] ['location']
        words [i] ['frequency'] +=i
        words [i] ['location'] = foo + "," + link
    if i not in words:
        words[i] = {}
        words[i] ['frequency'] = 1
        words[i] ['location'] = link


    def save(link):

        results = []
        results = datacollection(link)

        page_key = []
        for key in results.keys():
            page_key.append(key)
        for value in results.values():
            page_key.append(value)


    def build(num):
        initialpage(url)
        next1= "http://example.webscraping.com" +links[-1]
        pages(next1)
        prev = ""
        count2 = 0
        x = True

    while count2 <= num:
        print(count2)
        time.sleep(1)


class Spider(scrapy.Spider): 
      
    name = "crawl_spider"
      
    start_urls = 'http://example.webscraping.com/'
      
    # Parse function 
    def parse(self, response): 
          
        SET_SELECTOR = 'crawler'
        for geek in response.css(SET_SELECTOR): 
            pass




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




#ink = '<div id="pagination"><a href="/places/default/index/0">&lt; Previous</a><br><a href="/places/default/index/1">Next &gt;</a></div>'
#soup = BeautifulSoup(link, 'html.parser')


#pages_urls = [start_urls]

#soup = getAndParseURL(pages_urls[0])

# while we get two matches, this means that the webpage contains a 'previous' and a 'next' button
# if there is only one button, this means that we are either on the first page or on the last page
# we stop when we get to the last page

#while len(soup.findAll("a", href=re.compile("page"))) == 2 or len(pages_urls) == 1:
    
    # get the new complete url by adding the fetched URL to the base URL (and removing the .html part of the base URL)
    #new_url = "/".join(pages_urls[-1].split("/")[:-1]) + "/" + soup.findAll("a", href=re.compile("page"))[-1].get("href")
    
    # add the URL to the list
    #pages_urls.append(new_url)
    
    # parse the next page
    #soup = getAndParseURL(new_url)
    
#pages_urls = []

#new_page = "http://example.webscraping.com/places/default/index/2"
#while requests.get(new_page).status_code == 200:
    #pages_urls.append(new_page)
    #new_page = pages_urls[-1].split("-")[0] + "-" + str(int(pages_urls[-1].split("-")[1].split(".")[0]) + 1) + ".html"

#print(str(len(pages_urls)) + " fetched URLs")
#print("Some examples:")
#pages_urls[:25]

