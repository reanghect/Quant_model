#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import multiprocessing
from util import logger
from data import data_helper as hp
from data import data_worker as dw

__data_logger = logger.set_logger('data')
__author__ = 'Will Chen'

hp.loading_stock_list()
__data_logger.info('All ticker info created.')


pool = multiprocessing.Pool(processes=3)
stock_list = dw.get_stock_list()
for i in range(len(stock_list)):
    pool.apply_async(hp.loading_price, (stock_list[i], ))
__data_logger.info('Ready to load prices in 3 processes')
pool.close()
pool.join()
__data_logger.info('All price loaded into database')
