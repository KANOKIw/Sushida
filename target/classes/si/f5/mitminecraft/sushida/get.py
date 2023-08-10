import requests
from bs4 import BeautifulSoup
import json

url = "https://e-akane.com/blog/post-18198/"
d = 0
list = []
p = []
"""
def get_text_from_td(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        td_texts = []
        for td in soup.find_all("td"):
            td = str(td)
            if not td.startswith('<td height="18" style="height: 13.5pt;">'):continue
            p = td.replace('<td height="18" style="height: 13.5pt;">', "").replace("</td>", "")
            if (len(p) > 8): continue
            td_texts.append(p)
        return td_texts
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []


def _get_text_from_td(url):
    d = 1
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        td_texts = []
        for td in soup.find_all('td'):
            d += 1
            if d%2 == 0:
                td_texts.append(td.get_text())
        return td_texts
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []


res = _get_text_from_td(url)

with open(r"src\main\java\si\f5\mitminecraft\sushida\sushis.json", "w", encoding="utf-8") as f:
    json.dump(res, f, indent=4, ensure_ascii=False)
"""

p = []
with open(r"src\main\java\si\f5\mitminecraft\sushida\sushis.json", encoding="utf-8") as f:
    p = json.load(f)
smalls = ["ゃ","ゅ", "ょ","ぁ","ぃ","ぅ","ぇ","ぉ"]
ns = ["な", "に", "ぬ", "ね", "の"]
l = []
m = []
for word in p:
    for k in range(0, len(word)):
        try:
            if word[k] == "っ" and word[k+2] in smalls:
                p.remove(word)
                break
        except Exception as e:
            pass


with open(r"src\main\java\si\f5\mitminecraft\sushida\sushis.json", "w", encoding="utf-8") as f:
    json.dump(p, f, indent=4, ensure_ascii=False)

