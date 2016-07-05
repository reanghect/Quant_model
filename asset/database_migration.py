#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from playhouse.migrate import *
from . import database_model as db


__author__ = 'Will Chen'
migrator = MySQLMigrator(db.db)


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