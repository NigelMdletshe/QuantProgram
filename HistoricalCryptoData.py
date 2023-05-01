#Histrical data using Bitstamp API
import json
import requests
import pandas as pd
import datetime

start = "2021-11-01"
end = "2021-11-01"

pair ="btcusd"
parameters = {
    "step":60,
    "limit":10,
}
req = requests.get(f"https://www.bitstamp.net/api/v2/ohlc/{pair}",
                params= parameters )


req = req.json()["data"]["ohlc"]
df = pd.DataFrame(req)
print(df)