import tushare as ts

from asset import database_model as db
from util import logger
import requests
from datetime import datetime

__data_logger = logger.set_logger('data')


def __match_market(ticker):
    market_dict = {'600': 'SHA', '601': 'SHA', '603': 'SHA', '900': 'SHB',
                   '000': 'SZA', '001': 'SZA', '002': 'SZZX', '300': 'SZCY', '200': 'SZB'}
    try:
        market_id = market_dict[ticker[0:3]]
        return market_id
    except KeyError:
        print(ticker)


def __match_exchange(ticker):
    if ticker.startswith(('60', '90')):
        return 'XSHG'
    elif ticker.startswith(('00', '30', '20')):
        return 'XSHE'
    else:
        __data_logger.error(ticker)
        raise KeyError


def loading_price(record):
    today = datetime.strftime(datetime.now(), '%Y-%m-%d')
    # yesterday = datetime.datetime.strftime(datetime.datetime.now()-datetime.timedelta(1), '%Y-%m-%d')
    hist = ts.get_h_data(record.ticker, start='2014-01-01', end=today, autype='hfq', retry_count=10, pause=3)
    __data_logger.info(['Price loading for ' + record.ticker + ' begin'])
    for date in hist.index:
        str_date = date.strftime('%Y-%m-%d')
        db.DailyPrice.create(trading_date=str_date, ticker=record.ticker, market_id=record.market_id,
                             high=float(hist.get_value(date, 'high')), low=float(hist.get_value(date, 'low')),
                             open=float(hist.get_value(date, 'open')), close=float(hist.get_value(date, 'close')),
                             volume=float(hist.get_value(date, 'volume')))
    __data_logger.info(["Price Creation for stock " + record.ticker + " completed"])


def loading_stock_list():
    stock = ts.get_stock_basics()
    for inst in stock.index:
        market_id = __match_market(inst)
        exchangeCD = __match_exchange(inst)
        if market_id is not None:
            db.StockInfo.create(ticker=inst, market_id=market_id, asset_class='Equity', exchangeCD=exchangeCD,
                                short_name=stock.get_value(inst, 'name'), currency='CNY',
                                sector=stock.get_value(inst, 'industry'))
        else:
            __data_logger.error('can\'t find exchange name')
    __data_logger.info("Stock Info Creation Completed ")


def __get_calendar():
    domain = 'https://api.wmcloud.com:443/data/v1'
    path = '/api/master/getTradeCal.json'
    token = 'd97a4a4de8b42c7f270cd2ae478b476b4f05e9aecc4674d741fb7d09af8359e6'
    payload = {'field': None, 'exchangeCD': 'XSHG,XSHE', 'beginDate': '20140101'}
    response = requests.get(domain+path, params=payload, headers={"Authorization": "Bearer " + token})
    calen = response.json()
    if calen['retCode'] == 1:
        return calen['data']
    else:
        raise ConnectionError


def loading_calendar():
    try:
        calendar = __get_calendar()
        for each in calendar:
            trading_date = datetime.strptime(each['calendarDate'], '%Y-%m-%d')
            prev_date = datetime.strptime(each['prevTradeDate'], '%Y-%m-%d')
            db.TradingDate.create(date=trading_date, exchangeCD=each['exchangeCD'], isMonthEnd=bool(each['isMonthEnd']),
                                  isOpen=bool(each['isOpen']), isQuarterEnd=bool(each['isQuarterEnd']),
                                  isWeekEnd=bool(each['isWeekEnd']), isYearEnd=bool(each['isYearEnd']),
                                  prevTradeDate=prev_date)
    except ConnectionError as e:
        __data_logger.error(e)
