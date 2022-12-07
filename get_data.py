import pandas as pd

data = pd.read_csv(
    "./play-store-apps/googleplaystore.csv",
    header=0,
    skiprows=1,
)

print(data)
