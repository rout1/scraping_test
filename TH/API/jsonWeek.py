import requests
import json
from pprint import pprint
from datetime import datetime, timedelta, timezone
import pandas as pd
import matplotlib.pyplot
import japanize_matplotlib

url = "http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=metric"

url = url.format(city = "Hamamatsu,JP", key = "ca2fbedccb8451f2ce41c55921e2e2ec")

jsondata = requests.get(url).json()

pprint(jsondata)

print()
print("#########操作##########")
      
df = pd.DataFrame(columns = ["気温"])

tz = timezone(timedelta(hours = +9),'JST')
for dat in jsondata["list"] :
  jst = str(datetime.fromtimestamp(dat["dt"],tz))[:-9]
  df.loc[jst] = dat['main']['temp']
  #print("都市名:",jsondata['name'])
pprint(df)

df.plot(figsize=(15,8))
plt.ylim(-10,40)
plt.grid()
plt.show()