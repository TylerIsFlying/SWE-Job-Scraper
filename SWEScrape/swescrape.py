from bs4 import BeautifulSoup
import json
import re
import requests
tag_dict_list = []
def main():
    swe_job = SWEJobs()
    swe_job.load_jobs("swe-data")
class SWEJobs:
    def load_jobs(self,json_path: str) -> []:
        url = 'https://github.com/SimplifyJobs/Summer2025-Internships'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'lxml')
        table_tags = soup.find_all('tr')[10:]
        tag_dict_list = []
        for tag in table_tags:
            new_tag = ''.join(re.split(
                "<tr>|</tr>|<img[^>]*>|</img>|<summary>|</summary>|<td>|</td>|locations|<strong>|</strong>|",
                str(tag)))
            tag_dict = {'Company': self.extract_title(new_tag),
                        'URL': self.extract_url(new_tag),
                        'Role': self.extract_text_value(new_tag, 2),
                        'Location': self.extract_location(new_tag),
                        'Date Posted': self.extract_text_value(new_tag, 5)}
            tag_dict_list.append(tag_dict)
        with open(f"{json_path}.json", "w") as file:
            json.dump([dict(zip(d.keys(), d.values())) for d in tag_dict_list], file, indent=4)
    def extract_title(self,text):
        new_text = ''.join(re.split(r"</a[^>]*>|<a[^>]*>|<strong>|</strong>|</details>|<details>|", text))
        if '↳' in new_text.split('\n')[1]:
            return 'None'
        return new_text.split('\n')[1]
    def extract_url(self,text):
        new_text = re.findall(r'<a[^>]*href="([^" >#?]+)',text)
        return new_text
    def extract_text_value(self, text, index):
        new_text = text
        return new_text.split('\n')[index]
    def extract_location(self,text):
        new_text = ''.join(re.split("</a[^>]*>|<a[^>]*>|<strong>|</strong>|</details>|<details>|", text))
        return re.split(r'<br\/>|,|\+',new_text.split('\n')[3])
if __name__ == "__main__":
    main()