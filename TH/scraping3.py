import requests
from bs4 import BeautifulSoup as bs

url = "https://www.ymori.com/books/python2nen/test2.html"
HTML =requests.get(url)
soup = bs(HTML.content , "html.parser")

for element in soup.find_all("ol"):
    print(element.text)

e = soup.find(id = "chap2")

ol = e.find("ol").text

print(ol)

