import requests
import json
from bs4 import BeautifulSoup

# 1 taking the response of requests
res = requests.get("url-to-collect")

# 2 putting the encoding as "utf8" to collect Latin characters without being encoded
res.encoding = "utf-8"

# 3 parsing the soup
soup = BeautifulSoup(res.text, 'html.parser')

# 4 collecting the required data
resumes = soup.find(class_="box -flushHorizontal")
resumes1 = resumes.find('p').text
boxes = soup.find_all(id="producoes" ,class_="box -flush")
formations = soup. find_all(id="formacao" ,class_="box -flush inline-edit-main-box")
historic = soup.find_all(id="atuacao-profissional" ,class_="box -flush inline-edit-main-box")

# 5 extracting only the text inside the tags and organizing them within a dictionary
all_productions = []

for box in boxes:
    
    productions = (box.text)

for box in formations:

    formations1 = (box.text)

for box in historic:
    
    historic1 = (box.text)

all_productions.append({'resumo' : resumes1,'produções' : productions,'formações' : formations1,'histórico' : historic1}) 

# 6 saving the collected and translated data to a .json file
with open('boxs.json','w') as json_file:
    json.dump(all_productions, json_file, indent=3, ensure_ascii=False)