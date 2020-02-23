#% matplotlib inline
import requests
from bs4 import BeautifulSoup

load_url="https://www.ymori.com/books/python2nen/test2.html"
html=requests.get(load_url)
#response.encoding=response.apparent_encoding
soup=BeautifulSoup(html.content,"html.parser")

for element in soup.find_all("li"):
    print(element.text)
print(soup)
print()
print((soup.find(id="chap1").text))

print()
print(soup.find("h2"))
#filename="download.txt"
#with open(filename,mode="w") as f:
#    f.write(response.text)
