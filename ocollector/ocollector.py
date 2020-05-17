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
all_formations = []

formation = soup.find(id="body-education-list")
formations_list = formation.find_all(class_="col-md-9 col-sm-9 col-xs-7")

for formation in formations_list:
    formation1 = (formation.find(class_="workspace-title").text)
    year_formation = (formation.find(class_="affiliation-date").text)
    all_formations.append({ 'formation_title' : formation1, 'year' : year_formation})

with open('Orcid_formations.json', 'w') as json_file:
    json.dump(all_formations, json_file, indent=4)

# 4 finding fundings and "dump" them in json file as a dictionary
all_fundings = []
fundings = soup.find(id="workspace-fundings")
fundings_list = fundings.find_all(class_="col-md-9 col-sm-9 col-xs-7")

for funding in fundings_list:
    funding1 = (funding.find(class_="workspace-title").text)
    all_fundings.append({'funding' : funding1})

with open('Orcid_fundings.json', 'w') as json_file:
    json.dump(all_fundings, json_file, indent=4)

# 5 finding works and "dump" them in json file as a dictionary
all_works = []

works = soup.find(id="workspace-publications")
works_list = works.find_all(class_="col-md-9 col-sm-9 col-xs-7")

for work in works_list:
    work1 = (work.find(id="work.title").text)

    if(work.find(class_="journaltitle"))== None:
        journal_title = ""
    else:
        journal_title = (work.find(class_="journaltitle").text)
    year = (work.find(class_="info-detail").text)
    all_works.append({'title' : work1, 'journal' : journal_title, 'year' : year})

with open('Ocollector.json','w') as json_file:
    json.dump(all_works, json_file, indent=4)



