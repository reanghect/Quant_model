#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import multiprocessing
from util import logger
from data import data_helper as hp
from data import daily_data_worker as dw

__data_logger = logger.set_logger('data')
__author__ = 'Will Chen'

hp.loading_calendar()
__data_logger.info('Calendar Information loaded.')
hp.loading_stock_list()
__data_logger.info('All ticker info created.')


pool = multiprocessing.Pool(processes=3)
stock_list = dw.get_stock_list()
__data_logger.info('Ready to load prices in 3 processes')
for i in range(len(stock_list)):
    pool.apply_async(hp.loading_price, (stock_list[i], ))
pool.close()
pool.join()
__data_logger.info('All price loaded into database')
