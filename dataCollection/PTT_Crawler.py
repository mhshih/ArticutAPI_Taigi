# -*- coding: utf-8 -*-
"""
@author: simon
"""
import requests
from bs4 import BeautifulSoup
from string import punctuation, ascii_letters, digits

def ptt_scraping(url):
    articles = []
    r = requests.get(url=URL, cookies={"over18":"1"})
    soup = BeautifulSoup(r.text, "lxml")
    tag_divs = soup.find_all("div", class_="r-ent")
    for tag in tag_divs:
        if tag.find("a"):
            href = tag.find("a")["href"]
            title = tag.find("a").text
            
            r2=requests.get(url="http://ptt.cc"+href, cookies={"over18":"1"})
            soup2 = BeautifulSoup(r2.text, "lxml")
            articles.append({"title":title, "href":href, "text":soup2.text})
    return articles

URL = "http://ptt.cc/bbs/HatePolitics"
#URL = "http://ptt.cc/bbs/Gossiping"
print(URL)

articles = ptt_scraping(url=URL)
for i in range(5):
    article = articles[i]
    print("full-href", URL[:13] + article["href"])
    print("title", article['title'])
    filename = article["href"].split("/")[-1]
    with open(file=filename+".txt", mode="w", encoding="utf8") as file1:
        file1.write(article["text"])