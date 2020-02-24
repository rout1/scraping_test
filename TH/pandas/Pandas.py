import pandas as pd

df = pd.read_csv("python_sample/chap3/test.csv")

print(df)

print("################")

print(len(df))
print("項目：",df.columns.values)
print("インデックス:",df.index.values)

print()

print("国語のデータ\n",df[["国語"]])

print()

print("C子のdata\n",df.loc[[2]])

print("C子の理科の点数:",df.loc[2]["理科"])


