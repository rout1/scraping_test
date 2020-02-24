import requests
from bs4 import BeautifulSoup as bs
import urllib
from pathlib import Path
import time

print("GET!")

url = "https://news.yahoo.co.jp"
HTML =requests.get(url)

soup = bs(HTML.content , "html.parser")

out_folder = Path("yahooimg")
out_folder.mkdir(exist_ok = True)

print("WRITE!")

for element in soup.find_all("img"):

  src = element.get("src")
  
  image_url = urllib.parse.urljoin(url , src)
  imagedata = requests.get(image_url)
  filename = image_url.split("/")[-1]
  
  out_path = out_folder.joinpath(filename)
  
  with open(str(out_path),mode = "wb") as f:
    f.write(imagedata.content) 
    
  time.sleep(1)
    
print("Comprete!")


