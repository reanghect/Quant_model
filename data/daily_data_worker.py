from datetime import datetime

import tushare as ts
from pandas import Series

from asset import database_model as db
from asset import database_migration as dm
from util import logger

__module_logger = logger.set_logger("module")


def insert_daily_data():
    """
    Run every day after 15:00, collecting new market data and insert into DB
    """
    # dm.remove_index()
    update_list = db.StockInfo.select()
    today = datetime.today().strftime('%Y-%m-%d')
    for record in update_list:
        try:
            current = ts.get_h_data(code=record.ticker, start=today, end=today)
            str_date = current.index[0].strftime('%Y-%m-%d')
            row_id = db.DailyPrice.create(trading_date=str_date, ticker=record.ticker,
                                          market_id=record.market_id, high=float(current.high[0]),
                                          low=float(current.low[0]), open=float(current.open[0]),
                                          close=float(current.close[0]), volume=float(current.volume[0]))
            __module_logger.info('Insert ' + row_id + ' into Daily Price')
        except ConnectionError as e:
            __module_logger.debug(today + "Can't fetch daily data due to Connection Error")
            print(e)
    # dm.add_index()


def get_db_daily_price(fields, ticker=None, start=None, end=None, market=None, exchange=None):
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
    if exchange is not None:
        raw_data = raw_data.join(db.StockInfo).where(db.StockInfo.exchangeCD == exchange)
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



