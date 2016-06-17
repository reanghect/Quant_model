import tushare as ts
from util import logger
from datetime import datetime
from data import database_model as db
from pandas import Series
from data import database_migration as dm

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


def get_db_price(table='daily', ticker=None, start=None, end=None, fields=None):
    if table == 'daily':
        raw_data = db.DailyPrice.select(fields)\
            .where(db.DailyPrice.ticker == ticker, start < db.DailyPrice.trading_date < end)\
            .order_by(db.DailyPrice.trading_date)
    else:
        raw_data = db.IntraPrice.select(fields)\
            .where(db.IntraPrice.ticker == ticker, start < db.IntraPrice.time < end)\
            .order_by(db.IntraPrice.time)

    price = list()
    index = list()
    for record in raw_data:
        price.append(record.fields[0])
        index.append(record.trading_date[0])
    return Series(price, index=index)


def get_stock_list():
    l = []
    for stock in db.StockInfo.select():
        l.append(stock)
    return l
