from datetime import datetime

import tushare as ts
from pandas import Series

from asset import database_model as db
from asset import database_migration as dm
from util import logger

__module_logger = logger.set_logger("module")


def get_new_data():
    try:
        return ts.get_today_all()
    except ConnectionError as e:
        __module_logger.debug("Can't fetch new data due to Connection Error")
        print(e)


def insert_new_data(new_data):
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


def insert_daily_data():
    dm.remove_index()
    update_list = db.StockInfo.select(db.StockInfo.ticker)
    today = datetime.today().strftime('%Y-%m-%d')
    for record in update_list:
        try:
            current = ts.get_hist_data(code=record.ticker, start=today, end=today)
            db.DailyPrice.create(trading_date=current.index[0], ticker=record.ticker, market_id=record.market_id,
                                 high=float(current.high[0]), low=float(current.low[0]), open=float(current.open[0]),
                                 close=float(current.close[0]), volume=float(current.volume[0]))
        except ConnectionError as e:
            __module_logger.debug(today + "Can't fetch daily data due to Connection Error")
            print(e)
    dm.add_index()


def get_db_daily_price(fields, ticker=None, start=None, end=None, market=None):
    table = db.DailyPrice
    attr = [getattr(table, item) for item in fields]
    raw_data = table.select(*attr)
    if ticker is not None:
        raw_data = raw_data.where(table.ticker << ticker)
    if start is not None:
        raw_data = raw_data.where(table.trading_date > start)
    if end is not None:
        raw_data = raw_data.where(table.trading_date < end)
    if market is not None:
        raw_data = raw_data.where(table.market_id == market)
    raw_data = raw_data.order_by(table.trading_date)
    price = list()
    index = list()
    for record in raw_data:
        price.append(getattr(record, fields))
        index.append(record.trading_date[0])
    #     TODO Form a DataFrame  not list
    return Series(price, index=index)


def get_stock_list():
    l = []
    for stock in db.StockInfo.select():
        l.append(stock)
    return l



