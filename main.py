from bs4 import BeautifulSoup
import requests
url = 'https://github.com/SimplifyJobs/Summer2025-Internships'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'lxml')
table_tags = soup.find_all('table')
tr_tags = table_tags[1].find_all_next('tr')
for tr_tag in tr_tags:
    td_tags = tr_tag.find_all_next('td')
    print(td_tags)
