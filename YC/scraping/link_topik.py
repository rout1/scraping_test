#% matplotlib inline
import requests
from bs4 import BeautifulSoup
import urllib
load_url="https://news.yahoo.co.jp/"
html=requests.get(load_url)
#html.encoding=html.apparent_encoding

soup=BeautifulSoup(html.content,"html.parser")
topic=soup.find(class_="topics")
filename="yahoo.txt"
#print(topic)
with open(filename,mode="w") as f:
    for element in topic.find_all("a"):
        url=element.get("href")
        link_url=urllib.parse.urljoin(load_url,url)
        print(element.text)
        print(link_url)
        f.write(element.text+"\n")
        f.write(link_url+"\n")
        f.write("\n")

