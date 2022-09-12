import numpy as np
from scipy.stats import norm

'''
The Black-Scholes Model assumes that financial instruments such as option contracts and futures contracts will have a 
lognormal distribution of prices following a random walk with constant drift and volatility.

- No dividends are paid out during the life of the derivative
- Does not factor in broker fees
- Assumes a constant risk-free rate
- Returns of the underlying are normally distributed
'''


# US 10-yr Treasury Bond Rate  
interestRate = float(input('Interest rate: '))
# Current price of the underlying asset 
underlyingAsset = float(input('Price of underlying asset: '))
# Strike price of derivative
strikePrice = float(input('Option strike price: '))
# Days until derivative expires
timeToExpiry = float(input('Days to expiration: '))/365
# Dependent on your model, implied volatility is valid as well
volatility = float(input('Volatility: '))

def blackScholes(interestRate, underlyingAsset, strikePrice, timeToExpiry, volatility, type = "C"):
    d1 = (np.log(underlyingAsset/strikePrice) + (interestRate + volatility**2/2)*timeToExpiry) / (volatility*np.sqrt(timeToExpiry))
    d2 = d1 - volatility*np.sqrt(timeToExpiry)

    if type == "C":
        price = underlyingAsset*norm.cdf(d1, 0, 1) - strikePrice*np.exp(-interestRate*timeToExpiry)*norm.cdf(d2, 0, 1)
    elif type == "P":
        price = strikePrice*np.exp(-interestRate*timeToExpiry)*norm.cdf(-d2, 0, 1) - underlyingAsset*norm.cdf(-d1, 0, 1)
    else:
        print("Please re-confirm all option parameters listed above")
    return price

print('Option Price is: ', round(blackScholes(interestRate, underlyingAsset, strikePrice, timeToExpiry, volatility, type = "C"), 2))



