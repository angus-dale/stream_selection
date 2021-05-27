import pandas as pd
import random as rand
import sys

#Check arguments are structured correctly
try:
    if len(sys.argv) != 3:
        raise IndexError()
    filename = sys.argv[1] + ".csv"
    size = int(sys.argv[2])
except IndexError:
    raise SystemExit(f"Usage: {sys.argv[0]} <filename> <length>")
except ValueError:
    raise SystemExit("Length must be an integer")

#Initialise DataFrame
df = pd.DataFrame(columns=['feature1', 'feature2', 'feature3', 'target'])

#Add random valued rows for the requested length
for i in range(size):
    df = df.append({'feature1' : rand.randrange(-5,5), 'feature2' : rand.randrange(-5,5), 'feature3' : rand.randrange(-5,5), 'target' : rand.randrange(-5,5)},ignore_index=True)

#Write generated data to file
df.to_csv(f"data/{filename}", index=False)
