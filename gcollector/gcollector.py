import requests
import json
from bs4 import BeautifulSoup

# 1 using requests to get the page source
res = requests.get("url-to-collect")

# if necessary use "res.encoding = "windows1252"" to change encouding

# 2 using BeautifulSoup to parsing the page source
ind = 0
soup = BeautifulSoup(res.text, 'html.parser')

# 3 separating the data we want by class
gsces = soup.find_all(class_="gsc_a_tr")
texts = (soup.find_all(class_="gs_gray"))

all_texts1 = []
all_texts2 = []
all_productions = []

for i in range (len(texts)):
    if(i%2==0):
        text1 = ((texts[i]).text)
        all_texts1.append(text1)

for i in range (len(texts)):
    
    if(i%2!=0):
        
        text2 = ((texts[i]).text)
        all_texts2.append(text2)
        
# 4 collecting the data we want and organizing it in dictionary form
for gsc in gsces:
    titles = (gsc.find(class_="gsc_a_at").text)
    amount_of_citations = (gsc.find(class_="gsc_a_ac gs_ibl").text)
    year_of_publication = (gsc.find(class_="gsc_a_h gsc_a_hc gs_ibl").text)
    
    all_productions.append({'título' : titles,'text1' : all_texts1[ind],'text2' : all_texts2[ind],
    'citações' : amount_of_citations,'Ano' : year_of_publication})
    ind+=1

# 5 using the lib "json" to "dump" the dictionary to a json file
with open('gcollector.json','w') as json_file:
    json.dump(all_productions, json_file, indent=4)
    