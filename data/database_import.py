#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from util import logger
from data import data_helper as hp

__data_logger = logger.set_logger('data')
__author__ = 'Will Chen'

hp.loading_stock_list()
__data_logger.info('All ticker info created.')

threads = hp.building_thread()
for t in threads:
    t.setDaemon(True)
    t.start()

t.join()
__data_logger.info('All price loaded into database')
