import tushare as ts
from util import logger
from datetime import datetime
from data import database_model as db

_data_logger = logger.set_logger("module")


def get_new_data():
    try:
        return ts.get_today_all()
    except ConnectionError as e:
        _data_logger.debug("Can't fetch new data due to Connection Error")
        print(e)


def insert_new_data(new_data):
    time_stamp = datetime.now().time()
    for i in new_data.index:
        db.IntraPrice.create(ticker=new_data.ix[i].code, time=time_stamp, high=new_data.ix[i].high, low=new_data.ix[i].low,
                             open=new_data.ix[i].open, trade=new_data.ix[i].trade, change_percent=new_data.ix[i].changepercent)


def clean_intra():
    daily_delete = db.IntraPrice.delete()
    daily_delete.execute()


def insert_daily_data():
    update_list = db.StockInfo.select(db.StockInfo.ticker)
    today = datetime.today().strftime('%Y-%m-%d')
    for record in update_list:
        try:
            current = ts.get_hist_data(code=record.ticker, start=today, end=today)
            db.DailyPrice.create(trading_date=current.index[0], ticker=record.ticker, market_id=record.market_id,
                                 high=float(current.high[0]), low=float(current.low[0]), open=float(current.open[0]),
                                 close=float(current.close[0]), volume=float(current.volume[0]))
        except ConnectionError as e:
            print(e)


def get_db_price(ticker=None, start=None, end=None, fields=None, table='daily'):
    if table == 'daily':
        raw_data = db.DailyPrice.select(fields).where(db.DailyPrice.ticker == ticker,
                                                      start < db.DailyPrice.trading_date < end)
        return raw_data
        # return in DataFrame type
