import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import japanize_matplotlib

if __name__=='__main__':
  
  df=pd.read_excel("old31K.xls")
  df=df.set_index("年齢")
  print(df)
  
  fig, ax = plt.subplots(ncols=2, figsize=(10,6))
  ax[0].barh(df.index , df["男"], color='b', label='男')
  ax[0].yaxis.tick_right()
  ax[0].set_yticklabels([])
  ax[0].set_xlim([7000,0])
  ax[1].barh(df.index , df["女"], color='r', label='女')
  ax[1].set_xlim([0,7000])
  plt.title('西尾の人口ピラミッド(令和1年)',loc='left',size=19)
  fig.legend(loc='upper right')
  plt.savefig("OldPopulation.png")