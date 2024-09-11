import yfinance as yf
import pandas as pd

stock_symbol = 'AAPL'

stock_data = yf.download(stock_symbol, start = '2024-01-01', end= '2024-09-10')

# print(type(stock_data))
print(stock_data.head())

stock_data.to_csv('apple_stock_2024.csv')
