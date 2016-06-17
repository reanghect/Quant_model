#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from playhouse.migrate import *

__author__ = 'Will Chen'

my_db = MySQLDatabase("QSS", host="192.168.79.179", port=3306, user="will", passwd="Abc123")
migrator = MySQLMigrator(my_db)


def add_index(flag=False):
    migrate(
        migrator.add_index('DailyPrice', ('trading_date', 'ticker'), True),
    )
    if flag is True:
        migrate(
            migrator.add_index('StockInfo', ('ticker', 'market_id'), True),
        )


def remove_index():
    migrate(
        migrator.drop_index('DailyPrice', ('trading_date', 'ticker'))
    )