#
# Monte Carlo valuation of European call option
# in Black-Scholes-Merton model
# bsm_mcs_euro.py
#
import numpy as np
# Parameter Values
S0 = 100. # initial index level
K = 105. # strike price
T = 1.0 # time-to-maturity
r = 0.05 # riskless short rate
sigma = 0.2 # volatility
I = 100000 # number of simulations
# Valuation Algorithm
z = np.random.standard_normal(I) # pseudorandom numbers
ST = S0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * z)
# index values at maturity
hT = np.maximum(ST - K, 0) # inner values at maturity
C0 = np.exp(-r * T) * np.sum(hT) / I # Monte Carlo estimator
# Result Output
print("the value of the European call option is:",C0)


# Download Google stock price data from the Web.
# Calculate the rolling standard deviation of the log returns (volatility).
# Plot the stock price data and the results.

import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Retrieve data from Yahoo Finance
goog = web.DataReader('GOOG', data_source='yahoo', start='3/14/2009', end='4/14/2014')
print(goog.tail())

# Calculate volatility
goog['Log_Ret'] = np.log(goog['Close'] / goog['Close'].shift(1))
goog['Volatility'] = pd.Series(goog['Log_Ret']).rolling(window=252).std() * np.sqrt(252)

# Plot results
plt.style.use('ggplot')
goog[['Close', 'Volatility']].plot(subplots=True, color='blue', figsize=(8, 6))
plt.show()
