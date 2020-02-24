from pathlib import Path

out_folder = Path("down")
out_folder.mkdir(exist_ok=True)

filename = "konchiwa.txt"
filenamex = out_folder.joinpath(filename)

with open(str(filenamex) , mode = "w") as f:
  f.write("お前はよくやった\n")
