import yfinance as yf
import pandas as pd

symbols = ['AAPL','TSLA','MSFT']

data = yf.download(symbols,start='2024-01-01',end='2024-09-10')

print(type(data))

data.to_csv('multi_2024.csv')