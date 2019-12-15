import os
import requests
from bs4 import BeautifulSoup

# url source
url = "https://www.karir.com/search?context=welcome_main_search&q=web+developer&location=Prov.+DKI-Jakarta&IREFERRER=direct&LREFERRER=direct&ILANDPAGE=https%253A%2F%2Fwww.karir.com%2F&VISITS=1"

# url get response and set timeout connection
response = requests.get(url, timeout=10)

# parsing the content into html plain text
jobs = BeautifulSoup(response.content, "html.parser")

# content results
# print(jobs.prettify(), '\n')

row_opportunity = ('div', {'class': 'row opportunity-box'})

for all_positions in jobs:
    # print(jobs.find_all('div', {'class': 'row opportunity-box'}))
    print(jobs.find_all(row_opportunity))
    print(row_opportunity)
