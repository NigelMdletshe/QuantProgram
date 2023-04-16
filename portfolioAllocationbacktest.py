import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

weighting = {'BTC-USD':"50","ETH-USD":"50"}
members   = ['BTC-USD','ETH-USD']
basedata =yf.Ticker(members[0]).history(period="max").reset_index()[["Date","Open"]]
basedata['Date']=pd.to_datetime(basedata['Date'])
basedata = basedata.rename(columns= {"Open": members[0]})

if (len(members) > 1):
    for i in range(1,len(members)):
        newdata = yf.Ticker(members[i]).history(period="max").reset_index()[["Date","Open"]]
        newdata['Date']=pd.to_datetime(basedata['Date'])
        newdata = newdata.rename(columns= {"Open": members[i]})
        basedata = pd.merge(basedata, newdata, on="Date")

print(basedata)