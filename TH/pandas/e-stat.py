import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv("FEH_00200524_200224215658.csv", index_col="全国・都道府県",encoding="shift_jis")

df["平成30年"] = pd.to_numeric(df["平成30年"].str.replace(",",""))#データの数値にあるコンマ「,」を空白に替え、データタイプをobject型からint64型に変えた
df = df.drop("全国", axis=0)
df = df.sort_values("平成30年",ascending=False)
df["平成30年"].plot.bar(figsize=(20,10),title="平成30年の人口")
plt.show()

##昨年との差を出す
df["平成29年"] = pd.to_numeric(df["平成29年"].str.replace(",",""))

df["人口増減"]= df["平成30年"]-df["平成29年"]

df = df.sort_values("人口増減",ascending=False)
df["人口増減"].plot.bar(figsize=(10,6),title="増減")
plt.show()