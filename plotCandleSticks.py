import yfinance as yf
import pandas as pd
import mplfinance as mpf

df = yf.Ticker("BTC-USD").history(period="max")
print(df)
# something wrong with the environment