import pandas as pd

df = pd.read_csv("13TOKYO.CSV",header=None ,encoding = "shift_jis")
print(len(df))
print(df.columns.values)