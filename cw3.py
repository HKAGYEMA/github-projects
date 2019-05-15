from bs4 import BeautifulSoup
import requests
from time import sleep
import numpy
global index, iMap
index = []
iMap = []
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
    while '' not in sortSite:#for i in range(0, len(sortSite)-1):
        sortSite.remove('')
            #sortSite.pop(i)
    sortSite.sort()
    return sortSite

def invert(link,result):
    global index
    global iMap
    x= 0
    if index == []:
        index = result
        array = numpy.ones(len(result), numpy.int8)
        iMap.append([link, array.tolist()])
    else:
        tmp = []
        for word in index:
            if word not in result:
                tmp.append(0)
            else:
                count = 0
                try:
                    while result.remove(word) != ValueError:
                        count+=1
                except:
                    pass#print('')
                finally:
                    tmp.append(count)
        # Now add the rest to the list
        for y in range(len(result)):
            if y > 1 and result[y]==result[y-1]:
                tmp[-1] += 1
            elif y > 1 and result[y]!=result[y-1]:
                tmp.append(1)
                index.append(result[y])        
        iMap.append([link,tmp])
    x+=1
    #print(index, iMap)

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
            data = country_data(link+country[0]['href'])
            invert(link+country[0]['href'], data)
            print('* Success *',country[0]['href'])
        nav = getNext(page.text)
        #print(page.text)
        if nav == None:
            break
    return iMap,index

maps,index = run()
for row in maps:
    for i in range(len(row[1]),len(index)):
        row[1].append(0)
inp = 'Dollar'
if inp not in index:
    print(index)
    print('not in the index')
else:
    i = index.index(inp)
    #going through all the rows look for matching word
    for j in range(len(maps)):
        #print(index,'\n',maps[j][1], i)
        if maps[j][1][i] > 0:
            print('Site:\t',maps[j][0],'\nTimes:\t', maps[j][1][i])

#print (maps)
