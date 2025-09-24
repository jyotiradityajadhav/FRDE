import yfinance as yf

stocks = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'HINDUNILVR.NS',
          'ICICIBANK.NS', 'KOTAKBANK.NS', 'AXISBANK.NS', 'ITC.NS', 'SBIN.NS']

print("Downloading data...")
data = yf.download(stocks, period='6mo', auto_adjust=True)
data.to_csv('my_stocks.csv')
print("Done! Check 'my_stocks.csv' file")