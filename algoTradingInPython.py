#1 Data Gathering
#2 Backtesting 
#3 Execution Code
#4 Deploy bot to Cloud
#5 Trade analysis/Wrapup
#Get Data from Bistamp.

import json
import requests
import pandas as pd
import datetime


start = "2021-11-01"
end = "2021-11-10"

dates = pd.date_range(start, end, freq = "12H")
dates =[int(x.value/(10**9)) for x in list(dates)]
print(dates)

pair ="btcusd"
url = f"https://www.bitstamp.net/api/v2/ohlc/{pair}"
data = []
for first, last in zip (dates, dates[1:]):

    parameters = {
        "step":60, # change timeframe here
        "limit":1000,
        "start": first,
        "end":last
    }
    req = requests.get(url,
                params= parameters )


    req = req.json()["data"]["ohlc"]
    data += req


df = pd.DataFrame(data)
df = df.drop_duplicates()
df["timestamp"] = df["timestamp"].astype(int)
df = df[ df["timestamp"] >= dates[0]]
df = df[ df["timestamp"] < dates[-1]]

df["date"] = pd.to_datetime(df["timestamp"], unit = "s")
print(df)
print(len(df))
df.to_csv("data.csv")