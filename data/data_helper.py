import tushare as ts
from data import database_model as db
import logging
import threading


def match_market(ticker):
    market_dict = {'600': 'SHA', '601': 'SHA', '603': 'SHA', '900': 'SHB',
                   '000': 'SZA', '001': 'SZA', '002': 'SZZX', '300': 'SZCY', '200': 'SZB'}
    try:
        market_id = market_dict[ticker[0:3]]
        return market_id
    except KeyError:
        print(ticker)


def loading_price(stock_list):
    for record in stock_list:
        hist = ts.get_hist_data(code=record.ticker)
        logging.info(['Price loading for ' + record.ticker + ' begin'])
        for date in hist.index:
            db.Price.create(trading_date=date, ticker=record.ticker, market_id=record.market_id,
                            high=float(hist.get_value(date, 'high')), low=float(hist.get_value(date, 'low')),
                            open=float(hist.get_value(date, 'open')), close=float(hist.get_value(date, 'close')),
                            volume=float(hist.get_value(date, 'volume')))
        logging.info(["Price Creation for stock " + record.ticker + " completed"])
    logging.info("Price Creation for one stock exchange completed")


def loading_stock_list():
    stock = ts.get_stock_basics()
    for inst in stock.index:
        market_id = match_market(inst)
        if market_id is not None:
            db.StockInfo.create(ticker=inst, market_id=market_id, asset_class='Equity',
                                short_name=stock.get_value(inst, 'name'), currency='CNY',
                                sector=stock.get_value(inst, 'industry'))
        else:
            logging.error('can\'t find exchange name')
    logging.info("Stock Info Creation Completed ")


def building_thread():
    stock_sha = db.StockInfo.select(db.StockInfo.ticker).where(db.StockInfo.market_id == 'SHA')
    stock_sza = db.StockInfo.select(db.StockInfo.ticker).where(db.StockInfo.market_id == 'SZA')
    stock_oth = db.StockInfo.select(db.StockInfo.ticker)\
        .where((db.StockInfo.market_id != 'SHA') & (db.StockInfo.market_id != 'SZA'))
    threads = []
    t1 = threading.Thread(target=loading_price, name='Thread_SHA', args=[stock_sha])
    threads.append(t1)
    t2 = threading.Thread(target=loading_price, name='Thread_SZA', args=[stock_sza])
    threads.append(t2)
    t3 = threading.Thread(target=loading_price, name='Thread_OTH', args=[stock_oth])
    threads.append(t3)
    return threads
