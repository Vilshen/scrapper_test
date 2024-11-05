import requests
from bs4 import BeautifulSoup
import json

class Quote():
    def __init__(self, text,author,tags):
        self.text=text
        self.author=author
        self.tags=tags


url="https://quotes.toscrape.com/page/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
i=1
all_quotes=[]
while(True):
    print(f"Запрос страницы {i}")
    try:
        responce=requests.get(f"{url}+{i}",headers=headers)
    except:
        print("Не удалось получить страницу")
        break
    if responce.status_code==200:
        page_html=responce.text
        soup = BeautifulSoup(page_html, "html.parser")
        quotes=soup.findAll("div", class_="quote")
        if len(quotes)==0:
            break
        for quote in quotes:
            text=quote.find("span",class_="text")
            tags=quote.find("meta")["content"].split(',')
            author=quote.find("small",class_="author")
            all_quotes.append(Quote(text.text,author.text,tags))
    else:
        print(f"Не удалось получить данные, код{responce.status_code}")
        break;
    i+=1
out=json.dumps(all_quotes, indent=4, ensure_ascii=False, default=lambda x:{x.__class__.__name__:vars(x)})
f = open("output.json","w",encoding="utf-8")
f.write(out)
f.close()