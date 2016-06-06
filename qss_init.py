#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from data import database_model as db

import logging.config

__author__ = 'Will Chen'

CONF_LOG = "/conf/logger.conf"
logging.config.fileConfig(CONF_LOG)
logger = logging.getLogger()

logger.info("Welcome to QSS. System is preparing...")
db.drop_tables()
logger.info("Cleaned all tables, ready to begin...")
db.create_tables()
logger.info("Database Initialized. Ready to importing historical data")
