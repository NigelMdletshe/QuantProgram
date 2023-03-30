import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Read data from file 'data.csv'
df = pd.read_csv("BCHAIN-MKPRU.csv")
#print(df)
df = df[ df['Value'] > 0 ]
#df= df.iloc[::-1]
dates = pd.to_datetime(df['Date'])


# logaritmic function
def func(x,p1, p2):
    return p1 * np.log(x) + p2

# fitting data
ydata = np.log(df['Value'])
xdata = [ x + 1 for x in range(len(df))]
popt, pcov = curve_fit(func, xdata, ydata, p0=(3.0,-10))    

print("popt: ",popt)

fittedYdata = func(np.array([x for x in range(len(df))]),popt[0],popt[1])
plt.style.use('dark_background')

for i in range(-3,5):
    #plt.plot(dates,np.exp(fittedYdata + i)
    plt.fill_between(dates,np.exp(fittedYdata - i),np.exp(fittedYdata + i),alpha=0.4) 

plt.semilogy(dates,df['Value'])
plt.ylim(bottom = 1)
plt.show() 
