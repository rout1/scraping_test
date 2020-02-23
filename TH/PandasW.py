import pandas as pd

df = pd.read_csv("python_sample/chap3/test.csv")

df["体育"]=["50","80","80","80","80","80"]

print(df)

print("#############")

df.loc[6] = ["うん吾","3","100","8","90","90","1001"]

print(df)

