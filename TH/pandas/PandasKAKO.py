import pandas as pd

df = pd.read_csv("python_sample/chap3/test.csv")

data_s = df[df["数学"]>90]

print("数学成績優秀者\n",data_s)

print("数学最高点:",df["数学"].max())
print("数学最低点:",df["数学"].min())
print("数学平均点:",df["数学"].mean())
print("数学中央点:",df["数学"].median())
print("数学合計点:",df["数学"].sum())

print("ソートします。#####################")

data_sort = df.sort_values("理科")

print(data_sort)

data_sort = df.sort_values("理科",ascending=False)

print(data_sort)


print("転地#########################")

print(df.T)

print("リスト化#########################")

print(df.values)
