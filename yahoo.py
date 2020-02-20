import requests
from bs4 import BeautifulSoup as bs
import urllib

print("読み込み中")

url = "https://news.yahoo.co.jp"
HTML =requests.get(url)

HTML.encoding = HTML.apparent_encoding

soup = bs(HTML.content , "html.parser")

c = soup.find(class_ = "topics")
title = c.find_all("a")

print("書き込み中")

with open("yahoo.txt",mode = "w") as f:

  for element in title:
    URL = element.get("href")
    e = urllib.parse.urljoin(url,URL)#相対URLから絶対URLへ
    f.write(e)
    f.write("\n")

print("読み込み完了")
