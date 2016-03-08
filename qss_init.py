#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from data import database_model as db
import logging
__author__ = 'Will Chen'

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')

logging.info("Welcome to QSS. System is preparing...")
db.drop_tables()
logging.info("Cleaned all tables, ready to begin...")
db.create_tables()
logging.info("Database Initialized. Ready to importing historical data")
