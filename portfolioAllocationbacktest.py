import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

weighting = {'BTC-USD':"50","ETH-USD":"50"}
members   = ['BTC-USD','ETH-USD']
basedata =yf.Ticker(members[0]).history(period="max").reset_index()[["Date","Open"]]
basedata['Date']=pd.to_datetime(basedata['Date'])
basedata = basedata.rename(columns= {"Open": members[0]})

print(basedata)