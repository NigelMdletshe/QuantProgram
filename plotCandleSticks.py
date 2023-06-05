import yfinance as yf
import pandas as pd
import mplfinance as mpf

df = yf.Ticker("BTC-USD").history(period="max")
print(df)
# something wrong with the environment
df = df.loc["2018-01-01":]
mpf.plot(df, type = "candle", volume = True)