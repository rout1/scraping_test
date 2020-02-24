import pandas as pd
import folium

df = pd.read_csv("shokasen200.csv",encoding="shift-jis")

hydrand = df[["緯度","経度"]].values

m= folium.Map(location = [df["緯度"].mean(),df["経度"].mean()], zoom_start=16)

for data in hydrand :
  folium.Marker([data[0],data[1]]).add_to(m)

m.save('hydrant.html')
