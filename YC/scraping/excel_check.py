import pandas as pd 
import openpyxl

df=pd.read_csv("test.csv")

kokugo=df.sort_values("国語",ascending=False)#降順に並べる　ascending...昇順に並べる

df.to_excel("test.xlsx")


