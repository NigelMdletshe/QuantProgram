# API key: TLrA5GyGvmozbBmKFBy1 must be hidden
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('BCHAIN-MKPRU.csv')
df['200ma'] = df['Value'].rolling(window=1400).mean()
df=df[1400:]
dates = pd.to_datetime(df['Date'])

monthly=df[::30]
distance= monthly['200ma'].pct_change()*100

plt.style.use('dark_background')
plt.semilogy(dates, df['Value'], color='grey',zorder=1)
plt.semilogy(dates, df['200ma'],color='purple',zorder=2)

plt.scatter(monthly['Date'], monthly['Value'], c = distance, cmap = 'rainbow', vmin = 0, vmax = 16, zorder=3) 
cbar= plt.colorbar()
cbar.set_label('% montly increase in 200ma')
cbar.ax.yaxis.set_label_position('left')

plt.show()

#print(df.head())