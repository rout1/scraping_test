import requests as req
import json

def GET(URL):
  url='https://opendata.resas-portal.go.jp'
  filename='RESAS-API-key.txt'
  with open(filename , mode = 'r') as f:
    key = f.read()
  
  header = {"X-API-KEY":key}
  reqdata = req.get(url+'/'+URL , headers=header).json()
  
  return reqdata

if __name__ == '__main__':
  
  URL="api/v1/prefectures"
  print(GET(URL))
