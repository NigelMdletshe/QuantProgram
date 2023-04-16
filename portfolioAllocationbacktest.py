import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
#Get the data

weightings = {'BTC-USD':"50","ETH-USD":"50"} # test different weightings and symbols
members   = ['BTC-USD','ETH-USD']
#Add more weightings and symbols and print them
def PortfolioAllocation( weightings, data,name):
    data[name] = sum([int(weightings[x])*data[x]/100 for x in list(weightings.keys())])  
    return data

basedata =yf.Ticker(members[0]).history(period="max").reset_index()[["Date","Open"]]
basedata['Date']=pd.to_datetime(basedata['Date'])
basedata = basedata.rename(columns= {"Open": members[0]})

if (len(members) > 1):
    for i in range(1,len(members)):
        newdata = yf.Ticker(members[i]).history(period="max").reset_index()[["Date","Open"]]
        newdata['Date']=pd.to_datetime(newdata['Date'])
        newdata = newdata.rename(columns= {"Open": members[i]})
        basedata = pd.merge(basedata, newdata, on="Date")

basedata = basedata[basedata['Date'] > '2017-01-01']

for x in members:
    basedata[x] = basedata[x]/(basedata[x].iloc[0])

basedata = PortfolioAllocation(weightings, basedata, "Our Portfolio")
plt.plot(basedata['Date'], basedata['Our Portfolio'], label = "Our Portfolio")
plt.style.use('seaborn')
plt.legend(loc='upper left')
plt.show()
print(basedata)

#https://github.com/ChadThackray/pythontutorials/blob/main/code/Portfolio-allocation-backtesting.py