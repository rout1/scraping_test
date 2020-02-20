import requests

url = "https://www.ymori.com/books/python2nen/sample1.png"
imgdata = requests.get(url)

filename = url.split("/")[-1]

with open(filename , mode = "wb") as f:
  f.write(imgdata.content)
