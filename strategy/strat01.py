from data import data_worker as dw

# Current Data INPUT

hour_data = dw.get_new_data()

dw.insert_new_data(hour_data)


# Get Historical Data from DB

# Update Strategy status, trading signal output

# Save Current Data to DB
