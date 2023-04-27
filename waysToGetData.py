#data.Nasdaaq.com
#kaggle.com for long term 1min bars
#cryptodatadownload.com

import pandas as pd
df = pd.read_csv("BTCUSD.csv") # replace daily data with 1min data
df["date"] = pd.to_datetime(df["unix"],unit="s")
print(df)

#download 1min data

df.set_index("date",inplace=True)

#resample to 2min data
df2 = df.resample("2T").add({
    "open":"first",
    "high":"max",
    "low":"min",
    "close":"last"
})

print(df2)