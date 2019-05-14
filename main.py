from bs4 import BeautifulSoup
import requests
from time import sleep

def getNext(result):
    #result = requests.get(url)
    soup = BeautifulSoup(result, 'html.parser')
    
    child = soup.find_all('a')
    for i in range(0, len(child)):
        if 'Next' in child[i].get_text():
            nextlink = child[i]['href']
            return(nextlink)
    return None

def country_data(string):
    page = requests.get(string)
    soup = BeautifulSoup(page.text, 'html.parser')
    site = ""
    results = soup.find_all('tr')
    i = 0
    for result in results:
        table_data = result.findAll('td')
        soup2 = BeautifulSoup(table_data[1].text, 'html.parser')
        #skip empty strings
        if len(soup2.get_text().replace(" ","")) == 0:
            continue
        site += " "+soup2.get_text()
        i = 1+i
    # Remove empty things and sort them
    sortSite = site.split(" ")
    for i in range(0, len(sortSite)-1):
        if sortSite[i] == '':
            sortSite.pop(i)
    sortSite.sort()
    return sortSite


def run():
    nav = "" # used to navigate the website
    # Get the information from the web 
    link = 'http://example.webscraping.com/'
    while(1):
        page = requests.get('http://example.webscraping.com/'+nav)
        # Now get a list of all the countries
        soup = BeautifulSoup(page.text, 'html.parser')
        results = soup.find_all('td')
        for result in results:
            sleep(1)
            country = result.findChildren("a")
            print(country_data(link+country[0]['href']))
        nav = getNext(page.text)
        #print(page.text)
        if nav == None:
            break
run()
