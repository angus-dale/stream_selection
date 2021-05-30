import pandas as pd
import sys
from collections import defaultdict

#Check command line arguments
try:
    if len(sys.argv) != 2:
        raise IndexError()
    filename = "data/" + sys.argv[1] + ".csv"
except IndexError:
    raise SystemExit(f"Usage: {sys.argv[0]} <filename>")

#Load in data and split off target feature
data = pd.read_csv(filename)

target = data.pop(data.columns[-1])

#Initialise SV and SSV
svs = {}
ssvs = {}
counts = {}
selected = defaultdict(lambda: True)
for col in data.columns:
    val = data.at[0, col]
    svs[col] = {val}
    counts[col][val] = 1





