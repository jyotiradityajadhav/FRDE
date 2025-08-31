import pandas as pd
import numpy as np

# Read the CSV with proper handling
print("Reading your data...")
data = pd.read_csv('my_stocks.csv', header=[0, 1], index_col=0)

# Extract only the Close prices (ignore Volume data)
close_prices = data.xs('Close', axis=1, level=0, drop_level=True)

# Clean up the index (remove any text rows)
close_prices = close_prices[close_prices.index.str.contains('202')]  # Keep only date rows
close_prices.index = pd.to_datetime(close_prices.index)

# Calculate daily returns
print("Calculating returns...")
returns = close_prices.pct_change().dropna()

# Save to CSV
returns.to_csv('stock_returns_clean.csv')
print("Done! Clean returns saved to 'stock_returns_clean.csv'")

# Show preview
print("\nFirst 5 days of returns:")
print(returns.head())