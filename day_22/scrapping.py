# Day 22: 30 Days of python programming

# Web scrapping

# Exercises: Level 1

import requests
from bs4 import BeautifulSoup
import json

'''
1. Scrape the following website and store the data as json
file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
'''
url = 'http://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

data = {
    'title': soup.title.get_text(),
    'h1': soup.find('h1').get_text(),
    'h2': [c.get_text() for c in soup.find_all('h2')]
}

with open('./president.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

'''
2. Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file
'''
tables_url = 'https://archive.ics.uci.edu/ml/datasets.php'
res = requests.get(tables_url)
cont = res.content
tables_soup = BeautifulSoup(cont, 'html.parser')

tables = tables_soup.find_all('table', {'cellpadding':'3'})

tables_data = {}
table_counter = 1

for t in tables:
    table_name = f'table_{table_counter}'
    table_counter += 1
    tables_data[table_name] = {}
    row_counter = 1
    for tr in t.find_all('tr'):
        row_name = f'row_{row_counter}'
        row_counter += 1
        tables_data[table_name][row_name] = []
        for td in tr.find_all('td'):
            tables_data[table_name][row_name].append(td.text)

with open('./tables.json', 'w', encoding='utf-8') as f:
    json.dump(tables_data, f, ensure_ascii=False, indent=2)
