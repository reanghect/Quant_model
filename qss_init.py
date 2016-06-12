#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from data import database_model as db
from util import logger

_main_logger = logger.set_logger()

__author__ = 'Will Chen'

_main_logger.info("Welcome to QSS. System is preparing...")
db.drop_tables()
_main_logger.info("Cleaned all tables, ready to begin...")
db.create_tables()
_main_logger.info("Database Initialized. Ready to importing historical data")
