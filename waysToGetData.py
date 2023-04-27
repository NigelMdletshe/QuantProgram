#data.Nasdaaq.com
#kaggle.com for long term 1min bars
#cryptodatadownload.com
#Yfinance

import pandas as pd
import yfinance as yf


df = yf.Ticker("BTC-USD").history(period="1d", interval="1m")
print(df)
#resample to 2min data
df2 = df.resample("2T").agg({
    "Open":"first",
    "High":"max",
    "Low":"min",
    "Close":"last"
})
print(df2)

df2.to_csv("testdata.csv")
""" 
df = pd.read_csv("BTCUSD.csv") # replace daily data with 1min data
df.sort_values(by="unix", inplace = True)
df["date"] = pd.to_datetime(df["unix"],unit="s")
print(df)

#download 1min data

df.set_index("date",inplace=True)

#resample to 2min data
df2 = df.resample("2T").agg({
    "open":"first",
    "high":"max",
    "low":"min",
    "close":"last"
})

print(df2)
"""