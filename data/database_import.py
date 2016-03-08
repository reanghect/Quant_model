#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from data import data_helper as hp


__author__ = 'Will Chen'

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S', filename='data_import.log', filemode='w')

hp.loading_stock_list()
logging.info('All ticker info created.')

threads = hp.building_thread()
for t in threads:
    t.setDaemon(True)
    t.start()

t.join()
logging.info('All price loaded into database')
