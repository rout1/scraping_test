import pprint as pp
import RESAS_GET as g

def getpref(prefname):
  url='api/v1/prefectures'
  data = g.GET(url)
  for d in data['result']:
    if d['prefName']== prefname:
      global codeP
      codeP = d['prefCode']
      break
  
  return codeP


def getcity():
  
  url='api/v1/cities?prefCode='+ str(codeP)
  data = g.GET(url)
  pp.pprint(data)
  
  print("以下の市区町村がございます。")
  for d in data['result']:
    print(d['cityName'])
  
  cityname = input('市区町村名を入力ください:')
  
  for d in data['result']:
    if cityname == d['cityName']:
      if d['bigCityFlag'] == str(2):
        bCF = input('区分けされている都市です。区を特定しますか？(y/n):')
        if bCF == 'y':
          ku = input('区の名前を入力してください:')
          cityname = cityname + ku
          continue
      global codeC
      codeC = d['cityCode']
  
  return [codeC , cityname]


def getCamp():
  url="api/v1/municipality/company/perYear?cityCode="+ codeC+"&prefCode="+ str(codeP)
  data = g.GET(url)
  pp.pprint(data)
  
  result=data['result']['data'][3]['value']
  
  return result

if __name__ == '__main__':
  prefname = input("都道府県名を入力してください:")
  
  getpref(prefname)
  c = getcity()
  print(c[1]+"の企業数は"+ str(getCamp()))
  