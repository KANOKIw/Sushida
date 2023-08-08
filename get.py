import requests
from bs4 import BeautifulSoup
import json

url = "https://e-akane.com/blog/post-18198/"
list = []


def get(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        l = []
        for td in soup.find_all("td"):
            td = str(td)
            if not td.startswith('<td height="18" style="height: 13.5pt;">'):continue
            sushi = td.replace('<td height="18" style="height: 13.5pt;">', "").replace("</td>", "")
            if (len(p) > 8):continue
            l.append(sushi)
        return l
    else:
        print(f"Load failed!: {response.status_code}")
        return []

if __name__ == "__main__":
    sentences = get(url)

    with open(r"src\main\java\si\f5\mitminecraft\sushida\sushis.json", "w", encoding="utf-8") as f:
        json.dump(sentences, f, indent=4, ensure_ascii=False)
