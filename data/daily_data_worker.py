from datetime import datetime

import tushare as ts
from pandas import DataFrame, concat

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
    """
    :param fields: (List, Tuple, or String) open, close, high, low, volume
    :param ticker: (List, Tuple or String) Ex: ('600848', '000302')
    :param start: (String) YYYY-MM-DD
    :param end: (String) YYYY-MM-DD
    :param market: (List, Tuple, or String) Ex: ('SHA', 'SHB')
            Market Dictionary: {'600': 'SHA', '601': 'SHA', '603': 'SHA', '900': 'SHB',
                                '000': 'SZA', '001': 'SZA', '002': 'SZZX', '300': 'SZCY', '200': 'SZB'}
    :param exchange: (String) 'XSHE' or 'XSHG'
    :return: (DataFrame) order by trading_date, tickers are in columns;
    """
    table = db.DailyPrice
    if isinstance(fields, str):
        fields = {fields}
    else:
        fields = set(fields)
    fields.add('trading_date')
    fields.add('ticker')
    attr = [getattr(table, item) for item in fields]
    raw_data = table.select(*attr)
    if ticker is not None:
        if isinstance(ticker, (list, tuple)):
            t_ticker = tuple(ticker)
            raw_data = raw_data.where(table.ticker << t_ticker)
        elif isinstance(ticker, str):
            raw_data = raw_data.where(table.ticker == ticker)
        else:
            __module_logger.error('Ticker Parameter wrong' + ticker)
            raise ValueError
    if start is not None:
        raw_data = raw_data.where(table.trading_date > start)
    if end is not None:
        raw_data = raw_data.where(table.trading_date < end)
    if market is not None:
        if isinstance(market, (list, tuple)):
            market_temp = tuple(market)
            raw_data = raw_data.where(table.market_id << market_temp)
        elif isinstance(market, str):
            raw_data = raw_data.where(table.market_id == market)
        else:
            __module_logger.error('Market Parameter Wrong' + market)
            raise ValueError
    if exchange is not None:
        ticker_list = db.StockInfo.select(db.StockInfo.ticker).where(db.StockInfo.exchangeCD == exchange)
        raw_data = raw_data.where(table.ticker << ticker_list)
    raw_data = raw_data.order_by(table.market_id, table.ticker, table.trading_date).tuples()
    rows = list()
    for record in raw_data:
        rows.append(record)
    df = DataFrame(rows, columns=fields)
    df = df.set_index(['ticker', 'trading_date'])
    df_list = list()
    if len(ticker) > 1:
        for single_ticker in ticker:
            df_temp = df.loc[single_ticker]
            if len(df_temp.columns.values) > 1:
                df_temp.columns = [single_ticker + '_' + str(each)for each in list(df_temp.columns.values)]
            df_list.append(df_temp)
        new_df = concat(df_list, axis=1)
        return new_df
    else:
        return df


def get_stock_list():
    l = []
    for stock in db.StockInfo.select():
        l.append(stock)
    return l



