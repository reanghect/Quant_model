from data import daily_data_worker as dw

# Current Data INPUT

hour_data = dw.get_intra_data()

dw.insert_intra_data(hour_data)


# Get Historical Data from DB

# Update Strategy status, trading signal output

# Save Current Data to DB
