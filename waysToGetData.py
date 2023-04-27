#data.Nasdaaq.com
#kaggle.com for long term 1min bars
#cryptodatadownload.com

import pandas as pd
df = pd.read_csv("BTCUSD.csv")
df["date"] = pd.to_datetime(df["unix"],unit="s")
print(df)