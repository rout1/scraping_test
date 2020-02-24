import requests
import json
from pprint import pprint

url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=ja&units=metric"

url = url.format(city = "Hamamatsu,JP", key = "ca2fbedccb8451f2ce41c55921e2e2ec")

jsondata = requests.get(url).json()

pprint(jsondata)

print()
print("#########操作##########")

print("都市名:",jsondata['name'])
print("天気:",jsondata['weather'][0]['main'])
print("最高気温:",jsondata['main']['temp_max'], "\t最低気温:" , jsondata['main']['temp_min'])

