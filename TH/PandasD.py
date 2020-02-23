import pandas as pd

df = pd.read_csv("python_sample/chap3/test.csv")

df = df.drop("国語",axis=1)

print(df)

df = df.drop(2, axis=0)

print(df)

