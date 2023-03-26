# Chapter 1 of Python for finance by Yves Hilpisch
# Python for Finance, 2nd Edition
# (c) Dr. Yves J. Hilpisch | The Python Quants GmbH
# 
'''
a simple financial algorithm, namely the valuation of a European call option by Monte Carlo simulation.
We will consider a Black-ScholesMerton (BSM) setup (see also Chapter 3) in which the option’s underlying risk factor
follows a geometric Brownian motion.

Suppose we have the following numerical parameter values for the valuation:
Initial stock index level S0 = 100
Strike price of the European call option K = 105
Time-to-maturity T = 1 year
Constant, riskless short rate r = 5%
Constant volatility = 20%

In the BSM model, the index level at maturity is a random variable, given by Equation 1-1
with z being a standard normally distributed random variable.

Equation 1-1. Black-Scholes-Merton (1973) index level at maturity
# find equation 1-1 in the book page 

The following is an algorithmic description of the Monte Carlo valuation procedure:
1. Draw I (pseudo)random numbers z(i), i ∈ {1, 2, …, I}, from the standard normal
distribution.
2. Calculate all resulting index levels at maturity ST
(i) for given z(i) and Equation 1-1.
3. Calculate all inner values of the option at maturity as hT
(i) = max(ST
(i) – K,0).
4. Estimate the option present value via the Monte Carlo estimator given in Equation 1


'''
S0 = 100.
K = 105.
T = 1.0
r = 0.05
sigma = 0.2

import math 
import numpy 
from numpy import *
I = 100000
z = random.standard_normal(I)
ST = S0 * exp((r - 0.5 * sigma ** 2) * T + sigma * sqrt(T) * z)
hT = maximum(ST - K, 0)
C0 = exp(-r * T) * sum(hT) / I

print("the value of the European call option is:",C0)

