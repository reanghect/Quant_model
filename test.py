#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from decimal import Decimal
from pony.orm import *
from datetime import date

__author__ = 'Will Chen'

db = Database()
db.bind('mysql', host="192.168.70.106", user="qss", passwd="Abc123", db="qss_hist")


class Price(db.Entity):
    id = PrimaryKey(int, auto=True)
    trading_date = Required(date)
    full_id = Required(str, 20)
    high = Optional(Decimal)
    low = Optional(Decimal)
    open = Optional(Decimal)
    close = Optional(Decimal)
    adj_close = Optional(Decimal)
    volume = Optional(Decimal)


class TradingDate(db.Entity):
    id = PrimaryKey(int, auto=True)
    date = Required(date)
    isOpen = Required(str, 20)


class StockInfo(db.Entity):
    id = PrimaryKey(int, auto=True)
    full_id = Required(str, 20)
    market_id = Required(str, 20)
    asset_class = Required(str, 20)
    short_name = Required(str, 50)
    currency = Optional(str, 20)
    sector = Optional(str, 20)

sql_debug(True)
db.generate_mapping(create_tables=True)
