from bs4 import BeautifulSoup
import requests
import json
import time

# 1 using requests to get the page source
res = requests.get("url-to-collect")

# if necessary use "res.encoding = "windows1252"" to change encouding

# 2 using BeautifulSoup to parsing the page source
soup = BeautifulSoup(res.text, 'html.parser')

# 3 collecting the data boxes we want to collect by the class name
publications = soup.find_all(class_="data")

# 4 collecting the data we want and organizing it in dictionary form
all_publications = []

for publication in publications:
    author = publication.find(class_="this-person").text
    title = publication.find(class_="title").text
    year = publication.find(itemprop="datePublished").text
    all_publications.append({'author' : author, 'title' : title, 'year' : year})

# 5 using the lib "json" to "dump" the dictionary to a json file
with open('Dcollector.json', 'w' ) as json_file:
    json.dump(all_publications, json_file, indent=4)