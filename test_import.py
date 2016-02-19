#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import tushare as ts
import testpeewee as tp
import logging

__author__ = 'Will Chen'

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S', filename='data_import.log', filemode='w')

stock = ts.get_stock_basics()
market_id = 'SH'

for inst in stock.index:
    # TODO use dict to classify market_id, separate market_id and exch_id
    tp.StockInfo.create(ticker=inst, market_id=market_id, asset_class='stock',
                        short_name=stock.get_value(inst, 'name'), currency='CNY',
                        sector=stock.get_value(inst, 'industry'))

logging.info("Stock Info Creation Completed ")

for record in tp.StockInfo.select():
    hist = ts.get_hist_data(code=record.ticker)
    # TODO use multi-thread
    for date in hist.index:
        tp.Price.create(trading_date=date, ticker=record.ticker, exchId=record.market_id,
                        high=float(hist.get_value(date, 'high')), low=float(hist.get_value(date, 'low')),
                        open=float(hist.get_value(date, 'open')), close=float(hist.get_value(date, 'close')),
                        volume=float(hist.get_value(date, 'volume')))
    logging.info(["Price Creation for stock " + record.ticker + "completed"])
logging.info("Price Creation Completed")



