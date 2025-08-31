from nsepy import get_history
from datetime import date

# Get Reliance data example
data = get_history(symbol='RELIANCE',
                   start=date(2025,2,1),
                   end=date(2025,8,31))

data.to_csv('reliance_data.csv')
