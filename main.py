from bs4 import BeautifulSoup
import json
import re
import requests
url = 'https://github.com/SimplifyJobs/Summer2025-Internships'
page = requests.get(url)
def main():
    soup = BeautifulSoup(page.content, 'lxml')
    table_tags = soup.find_all('tr')[9:]
    table_dict = {}
    for tag in table_tags:
        new_tag = ''.join(re.split(
            "<tr>|</tr>",
            str(tag)))
        print(new_tag)

def extract_title(text):
    new_text = ''.join(re.split("</a[^>]*>|<a[^>]*>|<strong>|</strong>", text))
    return new_text
if __name__ == "__main__":
    main()