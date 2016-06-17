import tushare as ts
from data import database_model as db
from data import database_migration as dm
import threading
from util import logger

__data_logger = logger.set_logger('data')


def __match_market(ticker):
    market_dict = {'600': 'SHA', '601': 'SHA', '603': 'SHA', '900': 'SHB',
                   '000': 'SZA', '001': 'SZA', '002': 'SZZX', '300': 'SZCY', '200': 'SZB'}
    try:
        market_id = market_dict[ticker[0:3]]
        return market_id
    except KeyError:
        print(ticker)


def loading_price(record):
    hist = ts.get_hist_data(code=record.ticker, start='2015-01-01')
    __data_logger.info(['Price loading for ' + record.ticker + ' begin'])
    for date in hist.index:
        db.DailyPrice.create(trading_date=date, ticker=record.ticker, market_id=record.market_id,
                             high=float(hist.get_value(date, 'high')), low=float(hist.get_value(date, 'low')),
                             open=float(hist.get_value(date, 'open')), close=float(hist.get_value(date, 'close')),
                             volume=float(hist.get_value(date, 'volume')))
    __data_logger.info(["Price Creation for stock " + record.ticker + " completed"])


def loading_stock_list():
    stock = ts.get_stock_basics()
    for inst in stock.index:
        market_id = __match_market(inst)
        if market_id is not None:
            db.StockInfo.create(ticker=inst, market_id=market_id, asset_class='Equity',
                                short_name=stock.get_value(inst, 'name'), currency='CNY',
                                sector=stock.get_value(inst, 'industry'))
        else:
            __data_logger.error('can\'t find exchange name')
    __data_logger.info("Stock Info Creation Completed ")
