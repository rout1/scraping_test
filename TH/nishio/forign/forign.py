import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import japanize_matplotlib

if __name__=='__main__':
  
  year = 29
  
  df=pd.read_excel("f" + str(year) + ".xls")
  
  
  df = df.drop(len(df)-1,axis=0)
  df = df.set_index("国籍名")
  
  df = df.fillna(0)
  other = df[df["合計"] < 100]
  
  
  for o in other.index:
    df = df.drop(o,axis=0)
  
  df = df.sort_values("男",ascending = False)
  df.loc["その他"] = [other["男"].sum(),other["女"].sum(),other["合計"].sum()]
  
  df["合計"].plot.pie(label = '', fontsize=18 ,figsize = (8,8))
  plt.title("平成"+ str(year) +"年の西尾市の外国人割合", size=20)
  plt.savefig("nishio-forign-"+ str(year) + ".png")

