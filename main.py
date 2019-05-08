
from bs4 import BeautifulSoup
import requests
import re





main_url= "http://example.webscraping.com/"
result = requests.get(main_url)

soup = BeautifulSoup(result.text, 'html.parser')
def getAndParseURL(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    return(soup)

    
soup.find("a", class_ = "container") .div.a.get('href')

main_page_urls = [x.div.a.get('href') for x in soup.findAll("a", class_ = "container")]

print(str(len(main_page_products_urls)) + " fetched  URLs")
print("One example:")
main_page_urls[0]

def getWebsURLs(url):
    soup = getAndParseURL(url)
    # remove the index.html part of the base url before returning the results
    return(["/".join(url.split("/")[:-1]) + "/" + x.div.a.get('href') for x in soup.findAll("a", class_ = "container")])

categories_urls = [main_url + x.get('href') for x in soup.find_all("a", href=re.compile("a"))]
categories_urls = categories_urls[1:] 

print(str(len(categories_urls)) + " fetched  URLs")
print("Some examples:")
categories_urls[:5]

pages_urls = [main_url]
soup = getAndParseURL(pages_urls[0])

while len(soup.findAll("a", href=re.compile("page"))) == 2 or len(pages_urls) == 1:
 

new_url = "/".join(pages_urls[-1].split("/")[:-1]) + "/" + soup.findAll("a", href=re.compile("page"))[-1].get("href")

 # add the URL to the list
    pages_urls.append(new_url)
    
    # parse the next page
    soup = getAndParseURL(new_url)
    
    print(str(len(pages_urls)) + " fetched URLs")
    print("Some examples:")
    pages_urls[:25]
