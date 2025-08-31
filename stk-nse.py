from nsepy import get_history
from datetime import date

# Get Reliance data example
data = get_history(symbol='RELIANCE',
                   start=date(2023,1,1),
                   end=date(2023,12,31))
data.to_csv('reliance_data.csv')