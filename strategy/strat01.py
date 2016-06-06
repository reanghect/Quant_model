# Current Data INPUT

# Get Historical Data from DB

# Update Strategy status, trading signal output

# Save Current Data to DB

from data import data_worker as dw
from data import database_model as db
from datetime import datetime

time_window = datetime.date(2016, 4, 1)

new_data = dw.get_new_data()
raw_data = db.Price.select().where(db.Price.trading_date > time_window)
