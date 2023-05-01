#Histrical data using Bitstamp API
import json
import requests
import pandas as pd
import datetime

pair ="btcusd"
parameters = {
    "step":60,
    "limit":10,
}
req = requests.get(f"https://www.bitstamp.net/api/v2/ohlc/{pair}",
                params= parameters )
print(req)