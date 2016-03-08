#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from playhouse.migrate import *

__author__ = 'Will Chen'

my_db = MySQLDatabase("qss", host="192.168.70.154", port=3306, user="will", passwd="Abc123")
migrator = MySQLMigrator(my_db)

migrate(
    migrator.add_index('StockInfo', ('ticker', 'market_id'), True,),
    migrator.add_index('Price', ('trading_date', 'ticker', 'exchId'), True,)
)
