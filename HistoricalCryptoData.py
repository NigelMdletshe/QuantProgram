#Histrical data using Bitstamp API
import json
import requests
import pandas as pd
import datetime

start = "2021-11-01"
end = "2021-11-30"

dates = pd.date_range(start, end)
dates =[int(x.value/(10**9)) for x in list(dates)]
print(dates)

pair ="btcusd"

for first, last in zip (dates, dates[1:]):

    parameters = {
        "step":60,
        "limit":10,
        "start": first,
        "end":last
    }
    req = requests.get(f"https://www.bitstamp.net/api/v2/ohlc/{pair}",
                params= parameters )


    req = req.json()["data"]["ohlc"]


    df = pd.DataFrame(req)
    print(df)