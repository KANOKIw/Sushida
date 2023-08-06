import requests
from bs4 import BeautifulSoup
import json

url = "https://e-akane.com/blog/post-18198/"

def get(url):
    d = 1
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        td_texts = []
        for td in soup.find_all("td"):
            d += 1
            if d%2 == 0:
                td_texts.append(td.get_text())
        return td_texts
    else:
        print(f"Load failed!: {response.status_code}")
        return []

if __name__ == "__main__":
    list = get(url)

    with open(r"src\main\java\si\f5\mitminecraft\sushida\sushis.json", "w", encoding="utf-8") as f:
        json.dump(list, f, indent=4, ensure_ascii=False)
