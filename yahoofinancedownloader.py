# -*- coding: utf-8 -*-

# Importing necessary modules
import pandas_datareader.data as web
import pandas as pd

#Define what stocks (you can put as many as you want).
stocks = ['AAPL', 'MSFT', '^GSPC','GOOG','AMZN','TSLA']

#Select time period you want your stock prices denoted by format YYYY-MM-DD.
start_date = '2012-01-01'
end_date = '2016-12-31'

#Select intrval for stock prices
# Daily --> 'd'
# Weekly ---> 'w'
# Monthly ---> 'm'
interval = 'd'

# Select what price you want. Adjusted closed is by default.
# Other possible prices:
# 'High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close'
what_price = 'Adj Close'

stock_prices = pd.DataFrame(columns=stocks)
for stock in stocks:
    stock_data = web.get_data_yahoo(stock,start_date,end_date,interval=interval)
    stock_prices[stock] = stock_data[what_price]

#Saving it to the Excel file
stock_prices.to_excel('Stock_prices.xlsx')

# Calculate percent return of each stock
stock_returns = stock_prices.pct_change(fill_method='bfill')
stock_returns

# Save stock returns in an Excel file
stock_returns.to_excel('Stock_returns.xlsx')

