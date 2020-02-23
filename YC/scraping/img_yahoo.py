#% matplotlib inline
import requests
from bs4 import BeautifulSoup
import urllib
from pathlib import Path
import time

#フォルダを作成する
out_folder=Path("yahoo_download")
out_folder.mkdir(exist_ok=True)

load_url="https://news.yahoo.co.jp/"
html=requests.get(load_url)
soup=BeautifulSoup(html.content,"html.parser")



for element in soup.find_all("img"):
    src=element.get("src")
    image_url=urllib.parse.urljoin(load_url,src)
    imgdata=requests.get(image_url)
    time.sleep(1)
    
    filename=image_url.split("/")[-1]
    
    out_path=out_folder.joinpath(filename)
    with open(str(out_path),"wb") as f:
        f.write(imgdata.content)

