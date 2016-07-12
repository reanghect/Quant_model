from data import daily_data_worker as dw

# Current Data INPUT

# Get Historical Data from DB

fields = ['close', 'open']
ticker = ['600848', '000002']
start = '2014-01-02'
end = '2014-02-01'

raw = dw.get_db_daily_price(fields, ticker, start, end)
print(raw)
# Update Strategy status, trading signal output

# Save Current Data to DB
