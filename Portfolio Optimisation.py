# Portfolio Optimisation 


import numpy as np
import pandas as pd
from pandas_datareader import data as web
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# Stocks: 
stocks = ['BP.L', 'TOT.L', 'XOM', 'CVX', 'NG.L', 'CNA.L', 'SSE.L', 'UKW.L', 'PTR', 'PBR']

# Assign weights to stocks (equally weighted)
weights = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])

# Start/End dates
stock_StartDate = '2015-01-01'    
stock_EndDate = '2020-01-01'      

df = pd.DataFrame()     # dataframe to store adjusted close prices


# Store 'Adjusted Close' prices into the dataframe
for security in stocks:
    df[security] = web.DataReader(security, data_source='yahoo', start = stock_StartDate, end = stock_EndDate)['Adj Close']

print(df)       # show the dataframe

portfolio = df       # assign portfolio to the dataframe


# plot
for c in portfolio.columns.values:         
    plt.plot(portfolio[c], label = c)


# Generate plot
title = 'Portfolio Adjusted - Close Price History'  
plt.title(title)
plt.xlabel('Date', fontsize = 14)
plt.ylabel('Adj. Price USD($)', fontsize = 12)
plt.legend(portfolio.columns.values, loc = 'upper right')
plt.show()


# Daily simple return
daily_returns = df.pct_change()      # percentage change between current and prior element
print(daily_returns)


# Annualised covariance matrix (shows relationship between 2 stock prices)
cov_matrix_annual = daily_returns.cov() * 252             # daily returns MULTIPLIED 252 trading days
print(cov_matrix_annual)


# calculate portfolio variance (weights transposed MULTIPLIED covariance matrix, MULTIPLIED weights)
port_variance = np.dot(weights.T, np.dot(cov_matrix_annual, weights))       # weights transposed
print('Portfolio variance is: ', port_variance)


# calculate portfolio volitility (standard deviation)
port_volitility = np.sqrt(port_variance)
print('Portfolio volitility is: ', port_volitility)


# Annual portfolio return
portfolioSimpleAnnualReturn = np.sum(daily_returns.mean() * weights * 252)      # sum of average returns MULTIPLIED by trading days
print('Portfolio Simple Annual Returns is: ', portfolioSimpleAnnualReturn)


# Expected annual return, volitility (risk), variance
percent_var = str(round(port_variance, 2) * 100) + '%'                 # percent variance (round to 2 places)
percent_vols = str(round(port_volitility, 2) * 100) + '%'              # percent volitility (round to 2 places)
percent_ret = str(round(portfolioSimpleAnnualReturn, 2) * 100) + '%'   # percent return (round to 2 places)

print('Expected annual return: ', percent_var)
print('Annual volitiliy / risk: ', percent_vols)
print('Annual variance: ', percent_ret)





