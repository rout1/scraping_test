import pandas as pd

df=pd.read_csv("test.csv")

print(df)
print()
print(len(df))
print()
print(df.columns.values)#項目名（ヘッダ　科目名）
print()
print(df.index.values)#縦の人の番号
print()
print(df["国語"])
print()
print(df[["国語","英語"]])
print()
print(df.loc[1])
print()
print(df.loc[[0,1,2,4,5]])
print()
print(df.loc[1][2])#21と22は同じ結果
print(df.loc[1]["数学"])

df["美術"]=["68","73","82","77","94","96"]
df.loc[6]=["G恵","90","92","94","96","92","98"]

print(df)
