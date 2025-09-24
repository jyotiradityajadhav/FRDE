import pandas as pd
import numpy as np

print("Reading your data...")
data = pd.read_csv('my_stocks.csv', header=[0, 1], index_col=0)

close_prices = data.xs('Close', axis=1, level=0, drop_level=True)


close_prices = close_prices[close_prices.index.str.contains('202')]  
close_prices.index = pd.to_datetime(close_prices.index)

print("Calculating returns...")
returns = close_prices.pct_change().dropna()

returns.to_csv('stock_returns_clean.csv')
print("Done! Clean returns saved to 'stock_returns_clean.csv'")


print("\nFirst 5 days of returns:")
print(returns.head())