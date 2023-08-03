import yfinance as yf
import pandas as pd
import mplfinance as mpf

df = yf.Ticker("BTC-USD").history(period="max")
df = df.loc["2021-01-01":] # Caps the data
mpf.plot(df, type="candle", volume = True , mav = (10,3.20))

#print(df)
#df["50ma"] = df["Open"].rolling(windows=50).mean()/1.5
#df["ma"] = df["Open"].rolling(windows=50).mean()*1.5
#apds = [ mpf.make_addplt(df["50ma","ma"])]
# something wrong with the environment
#df = df.loc["2018-01-01":]
#mpf.plot(df, type = "candle", volume = True,mav=(10,3,20),addplot = apds)