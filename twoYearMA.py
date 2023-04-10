import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("BCHAIN-MKPRU.csv")
df= df.iloc[::-1]
df['Date']=pd.to_datetime(df['Date'])

df['2yma'] = df['Value'].rolling(window=730).mean()
df['2yma5'] = 5*df['2yma']

df = df[df['Date'] > '01.01.2012']

plt.style.use("dark_background")

plt.semilogy(df['Date'], df['Value'], color = 'grey', label ="Bitcoin Price")
plt.semilogy(df['Date'], df['2yma'],  color = 'green', label = "2 Year Moving Average")
plt.semilogy(df['Date'], df['2yma5'], color = 'red', label= "5x 2 Year Moving Average")

plt.fill_between(df['Date'], df['2yma5'], df['Value'],color='red', alpha=0.4, where = list(df['Value'] > df['2yma5']))
plt.fill_between(df['Date'], df['Value'], df['2yma'],color='green', alpha=0.4, where = list(df['Value'] < df['2yma']))


plt.ylim(ymin = 1)
plt.title("Bitcoin Price")
plt.xlabel("Date")
plt.ylabel("Price (USD)")

plt.legend()

plt.show()

