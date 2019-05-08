import requests
from parsel import Selector
import openpyxl as op
import pandas as pd

import time
start = time.time()



all_links = []
response = requests.get('http://example.webscraping.com')
selector = Selector(response.text)
href_links = selector.xpath('//a/@href').getall()
all_links += href_links

sheet_name = "URLs"

for link in href_links:
	    try:
	        response = requests.get(link)
	        selector = Selector(response.text)
	        href_links = selector.xpath('//a/@href').getall()
	        all_links += href_links
	        if len(all_links) >=1000:
	          break
	    except Exception as exp:
	        print('Error navigating to link : ', link)
print(all_links)
end = time.time()
print("Time taken in seconds : ", (end-start))

soup = BeautifulSoup("")
urls = soup.findAll("a")

    # Even if the url is not part of the same domain, it is still collected
    # But those urls not in the same domain are not parsed
    for a in urls:
        if (a.get("href")) and (a.get("href") not in url_list):
            url_list.append(a.get("href"))

def load_to_excel(lst):
    """
    Load the list into excel file using pandas
    """
    # Load list to dataframe
    df = pd.DataFrame(lst)
    df.index += 1  # So that the excel column starts from 1

    # Write dataframe to excel
    xlw = pd.ExcelWriter(xl_name)
    df.to_excel(xlw, sheet_name=sheet_name, index_label="#", header=["URL"])
    xlw.save()

