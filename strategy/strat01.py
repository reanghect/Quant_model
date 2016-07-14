from data import daily_data_worker as dw
import talib
import numpy as np
import pandas as pd
# Current Data INPUT

# Get Historical Data from DB

start = '2014-01-01'
end = '2016-07-08'

raw = dw.get_db_daily_price('close', start=start, end=end)

for i in raw.columns:
    test = np.array(raw[i].values, dtype=float)
    shortSMA = talib.SMA(test, 5)
    longSMA = talib.SMA(test, 10)
    MACD = talib.MACD(test)
    # output = pd.DataFrame([shortSMA, longSMA], index=raw.index)
#     TODO change DataFrame into list(tuple) containing dict or a generator(if too large)
    raw_output = None
    dw.db.TechIndicator.insert_many(raw_output)

# Update Strategy status, trading signal output

# Save Current Data to DB
