import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv("python_sample/chap3/test.csv")

df.plot.bar()
plt.legend(loc = "lower right")
plt.show()

df.plot.barh()
plt.legend(loc = "lower right")
plt.show()

df.plot.bar(stacked = True)
plt.legend(loc = "lower right")
plt.show()

df.plot.box()
plt.legend(loc = "lower right")
plt.show()

df.plot.area()
plt.legend(loc = "lower right")
plt.show()
