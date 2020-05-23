from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time

# 1 open webdriver with selenium and catch page_souce 
driver = webdriver.Chrome()
driver.get("url-to-collect")

#if necessary use "time.sleep(10)" to ensure that the data will all be loaded before collection

html = (driver.page_source)

# 2 parsing the page_source with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# 3 finding formations and "dump" them in json file as a dictionary
all_works = []

works = soup.find_all(class_="searchArea")

# 4 collecting the data we want and organizing it in dictionary form
for work in works:
    
    # Using the 'findChrildren' method to be able to separate and thus collect the data
    children = work.findChildren('td')
    
    work_title = (work.find(class_="docTitle").text)
    # If you want to collect only the first author
    # author = (work.find(class_="previewTxt").text) 
    authors = ((children[1]).text)
    year = ((children[2]).text)
    source = ((children[3]).text)
    cited = ((children[4]).text)

    all_works.append({ 'title' : work_title, 'author' : authors, 'year' : year, 'source' : source, 'cited by' : cited})

# 5 using the lib "json" to "dump" the dictionary to a json file
with open('scollector.json', 'w') as json_file:
    json.dump(all_works, json_file, indent=4)