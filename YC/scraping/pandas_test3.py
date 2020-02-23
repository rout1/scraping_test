import pandas as pd 
from pathlib import Path
df=pd.read_csv("test.csv")
print(df)
print("数学の最高点＝"+str(df["数学"].max()))
print("数学の最低点＝"+str(df["数学"].min()))
print("数学の平均点＝"+str(df["数学"].mean()))
print("数学の中央値＝"+str(df["数学"].median()))
print("数学の合計＝"+str(df["数学"].sum()))

df=df.sort_values("数学")
print(df)
#df=df.sort_values("数学",ascending=False)

out_folder=Path("数学の順番")
out_folder.mkdir(exist_ok=True)

out_path=out_folder.joinpath("math_result.csv")
df.to_csv(str(out_path))


out_path=out_folder.joinpath("math_result2.csv")
df.to_csv(str(out_path),index=False)

out_path=out_folder.joinpath("math_result3.csv")
df.to_csv(str(out_path),index=False,header=False)



print(df)
print(df.values)
print(df.T)

print(df.T.values)
