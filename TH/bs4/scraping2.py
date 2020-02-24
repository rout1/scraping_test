import requests
from bs4 import BeautifulSoup as bs

url = "https://www.ymori.com/books/python2nen/test1.html"
HTML =requests.get(url)
soup = bs(HTML.content , "html.parser")

print(soup)

print("##################title　抽出####################")

print(soup.find("title"))

print("#################文字列のみ　抽出#####################")

print(soup.find("h2").text)

print("################リスト　抽出######################")

print(soup.find("ol"))


