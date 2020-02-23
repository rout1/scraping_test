import pandas as pd

df=pd.read_csv("test.csv")


print(df)
print("data length is "+str(len(df)))
print("columns is " + str(df.columns.values))
print("index is"+ str(df.index.values))
print("data length is "+str(len(df.columns.values)))#このやり方でインデックスの長さも出せる。
print("columns length is "+ str(len(df.index.values)))
print("c子のデータ"+ str(df.loc[2]))
print("c子の国語"+ str(df.loc[2]["国語"]))
df["体育"]=[1,2,3,4,5,6]
df.loc[6]=["G助",1,2,3,4,5,7]

df=df.drop("数学",axis=1)
df=df.drop(1,axis=0)
print("\n")
print(df)

print("\n"*3)

print(df["国語"]>=90)
print(df[df["国語"]>=90])


