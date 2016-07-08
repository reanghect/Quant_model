from datetime import datetime

import tushare as ts


from asset import database_model as db
from util import logger

__module_logger = logger.set_logger("module")


def get_intra_data():
    try:
        return ts.get_today_all()
    except ConnectionError as e:
        __module_logger.debug("Can't fetch new data due to Connection Error")
        print(e)


def insert_intra_data(new_data):
    time_stamp = datetime.now().time()
    for i in new_data.index:
        db.IntraPrice.create(ticker=new_data.ix[i].code, time=time_stamp, high=new_data.ix[i].high,
                             low=new_data.ix[i].low, open=new_data.ix[i].open, trade=new_data.ix[i].trade,
                             change_percent=new_data.ix[i].changepercent)
        __module_logger.debug("Insert " + str(time_stamp) + " hourly data into IntroPrice")


def clean_intra():
    daily_delete = db.IntraPrice.delete()
    daily_delete.execute()
    __module_logger.debug("Delete IntraPrice daily")