import yfinance as yf
import pandas as pd
import mplfinance as mpf

df = yf.Ticker("BTC-USD").history(period="max")


df["50ma"] = (df["Open"].rolling(window=50).mean())/ 1.5
df["ma"] = (df["Open"].rolling(window=50).mean())*1.5

df = df.loc["2021-01-01":] # Caps the data

apds = [ mpf.make_addplot(df[["50ma","ma"]])]

df = df.loc["2021-01-01":] # Caps the data

mpf.plot(df, type="candle", volume = True , addplot = apds)







