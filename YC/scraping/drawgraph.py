import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

#df=pd.read_csv("test.csv")
df=pd.read_csv("test.csv",index_col=0)
print(df)

df["国語"].plot.barh()
plt.legend(loc="lower left")

plt.show()

df[["国語","数学"]].plot.barh()
plt.legend(loc="lower left")
plt.show()

df.loc["C子"].plot.barh()
plt.legend(loc="lower left")
plt.show()

df.loc["C子"].plot.pie()
plt.legend(loc="lower left")
plt.show()

df.T.plot.barh()
plt.legend(loc="lower right")
plt.savefig("bargraph.png")
plt.show()

