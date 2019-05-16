from bs4 import BeautifulSoup
import requests
from time import sleep
import numpy
import json


global index, iMap
index = []
iMap = []

## Get the links for the next page in the website
def getNext(result):
    soup = BeautifulSoup(result, 'html.parser')
    
    child = soup.find_all('a')
    for i in range(0, len(child)):
        if 'Next' in child[i].get_text():
            nextlink = child[i]['href']
            return(nextlink)
    return None

## Get the data from the country specific page
def country_data(string):
    page = requests.get(string)
    soup = BeautifulSoup(page.text, 'html.parser')
    site = ""
    results = soup.find_all('td')

    for result in results:

        if len(result.text.replace(" ","")) == 0:
            continue
        site += " "+result.text.replace(":","")

    # Remove empty things and sort them
    sortSite = site.split(" ")
    while '' not in sortSite:
        sortSite.remove('')
    sortSite.sort()
    return sortSite

## Do the inverted index in the form of a table to keep a track of each word
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

# 
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
        if nav == None:
            break
    return iMap,index
#'''
def build():
    maps,index = run()
    # Now add zeros to the index words left out
    for row in maps:
        for i in range(len(row[1]),len(index)):
            row[1].append(0)
    # Load into a json file
    x={}
    for i in range(len(index)):
        lst = []
        for j in maps:
            if j[1][i] > 0:
                lst.append([j[0],j[1][i]])
        #lstS = {lst}
        x.update({index[i]: lst})
        # convert into JSON:
        with open('Countries.json','w') as f:
            f.write(json.dumps(x,sort_keys=True, indent=2))
            # the result is a JSON string:

# Read the file from json and load it  
def load():
    datastore = None
    # create and build if the file is not there
    try:
        with open('Countries.json') as jsn:
            datastore = json.load(jsn)
    except FileNotFoundError or FileExistsError:
        print('File does not exist Building now')
        build()
        with open('Countries.json') as jsn:
            datastore = json.load(jsn)
    return datastore

## Find two words which can be seen in multiple files
def find(word1,word2):
    lines = load()
    matches = 0
    try:
        specific1 = lines[word1]
        specific2 = lines[word2]
        print('[',word1,"] and [", word2,']')
        for line1 in specific1:
            if line1 in specific2:
                matches = 1
                print('\t',line1)
        if matches == 0:
            print('No match found for [',word1,'&',word2,']')
    except KeyError:
        print("Word Does not exist in dataset")

def cPrint(words):
    lines = load()
    try:
        specific = lines[words]
        print(words)
        for line in specific:
            print('\t',line[0])
    except KeyError:
        print("Word Does not exist in dataset")
# Menu for User
if __name__ == "__main__":
    while(1):
        print("#################################")
        print("Enter one of the Listed commands:\n")
        print("[*]Build\n[*]Load\n[*]Print\n[*]Find\n[*]Exit")
        usrIn = input("Enter option: ")
        #print(usrIn.lower())
        if usrIn.lower() == 'build':
            build()
        elif usrIn.lower() == 'load':
            print(load())
        elif usrIn.lower() == 'print':
            word = input("Enter the word to search 4: ")
            cPrint(word)
        elif usrIn.lower() == 'find':
            usrFind = input('Enter words to search for\n E.g."Dollar AF":')
            usrFind = usrFind.split(" ")
            if len(usrFind) == 2:
                find(usrFind[0], usrFind[1])
        elif usrIn.lower()=='exit':
            break
        else:
            print('Please enter the right command according to the menu\n')
