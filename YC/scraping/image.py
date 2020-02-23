#% matplotlib inline
import requests
from bs4 import BeautifulSoup
import urllib
from pathlib import Path

#フォルダを作成する
out_folder=Path("download")
out_folder.mkdir(exist_ok=True)



load_url="https://www.ymori.com/books/python2nen/sample1.png"
imgdata=requests.get(load_url)
#html.encoding=html.apparent_encoding

filename=load_url.split("/")[-1]
out_path=out_folder.joinpath(filename)

print(filename)
print(out_path)
print(type(out_path))
with open(str(out_path),mode="wb") as f:
        f.write(imgdata.content)

