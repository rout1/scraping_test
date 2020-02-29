import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import japanize_matplotlib

def getpopu(filename,month,year):#必要な情報のみを抽出
  Y='平成'+str(year)+'年度'
  df = pd.read_excel(filename,sheet_name="年度",index_col=Y)
  df = df.T
  return df[month].values

if __name__=='__main__':
  
  month=4#抽出する月を決める
  
  choose="総人口"#グラフ化する要素を入力
  
  colu=["日本人","外国人","総人口","日本人男性","日本人女性","外国人男性","外国人女性","基本世帯数","外国人世帯数","総世帯数"]#要素
  year31 = getpopu("20191108-170947.xlsx",month,31)
  year30 = getpopu("20190311-164547.xls",month,30)
  year29 = getpopu("20180302-154018.xls",month,29)
  year28 = getpopu("20170307-092858.xls",month,28)
  year27 = getpopu("20170307-092833.xls",month,26)
  year26 = getpopu("20170307-092426.xls",month,27)
  year25 = getpopu("20170307-092333.xls",month,25)
  
  popudata = pd.DataFrame([year25,year26,year27,year28,year29,year30,year31],columns=colu)#人口関係のデータのみにまとめたDataFrameを新規作成
  
  popudata["年度"]=["25年度","26年度","27年度","28年度","29年度","30年度","31年度"]
  popudata = popudata.set_index("年度")#index変更
  print(popudata)
  
  popudata[[choose]].plot.bar(title="西尾の"+choose,figsize=(10,6))
  plt.ylim(169000,173000)
  plt.legend(loc="lower left")
  plt.savefig("population.png")