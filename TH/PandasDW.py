import pandas as pd
from pathlib import Path

pathout = Path("python_sample")
pathout.mkdir(exist_ok = True)
pathin_name="chap3"
pathname = pathout.joinpath(pathin_name)

pathin = Path(str(pathname))
pathin.mkdir(exist_ok = True) 

fd = pd.read_csv("python_sample/chap3/test.csv")

kokugo = fd.sort_values("国語",ascending= False)

filename="export1.csv"
filenamex=pathin.joinpath(filename)

kokugo.to_csv(str(filenamex),index=False,header=False)
print(str(filenamex))






