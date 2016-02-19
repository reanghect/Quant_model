#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from peewee import *

__author__ = 'Will Chen'


db = MySQLDatabase("qss", host="192.168.70.154", port=3306, user="will", passwd="Abc123")


class BaseModel(Model):
    class Meta:
        database = db


class Price(BaseModel):
    id = PrimaryKeyField()
    trading_date = DateField()
    ticker = CharField(20)
    exchId = CharField(20)
    high = DecimalField(decimal_places=2, null=True)
    low = DecimalField(decimal_places=2, null=True)
    open = DecimalField(decimal_places=2, null=True)
    close = DecimalField(decimal_places=2, null=True)
    volume = FloatField(null=True)

    class Meta:
        # multiple column index or multiple indexes
        indexes = ((('trading_date', 'ticker', 'exchId'), True),)


class TradingDate(BaseModel):
    id = PrimaryKeyField()
    date = DateField(unique=True)
    isOpen = CharField(20)


class StockInfo(BaseModel):
    id = PrimaryKeyField()
    ticker = CharField(20, unique=True)
    market_id = CharField(20)
    asset_class = CharField(20)
    short_name = CharField(50, unique=True)
    currency = CharField(10)
    sector = CharField(20)

    class Meta:
        indexes = ((('ticker', 'market_id'), True),)


class Account(BaseModel):
    id = PrimaryKeyField()
    account_number = CharField(20)


class OrderInfo(BaseModel):
    id = PrimaryKeyField()
    account = ForeignKeyField(Account)
    ticker = CharField(20)
    market_id = CharField(20)
    order_time = DateTimeField()
    order_qty = IntegerField()
    bs_flag = CharField(10)
    order_price = DecimalField(decimal_places=2)
    exchange_type = CharField()


class Settlement(BaseModel):
    id = PrimaryKeyField()
    account = ForeignKeyField(Account)
    bs_flag = CharField(10)
    exchange_type = CharField(20)
    ticker = CharField(20)
    market_id = CharField(20)
    deal_amount = IntegerField()
    deal_price = DecimalField(20)
    deal_time = DateTimeField()
    commission = DecimalField()


class Cash(BaseModel):
    id = PrimaryKeyField()
    account = ForeignKeyField(Account)
    involved_amount = DecimalField(decimal_places=2)
    post_usable_amount = DecimalField(decimal_places=2)
    currency = CharField(20)
    frozen_amount = DecimalField(decimal_places=2, default=0)


class Position(BaseModel):
    id = PrimaryKeyField()
    exchange_type = CharField(20)
    ticker = CharField(20)
    market_id = CharField(20)
    quantity = IntegerField()
    average_price = DecimalField(decimal_places=2)
    latest_price = DecimalField(decimal_places=2)
    market_value = DecimalField(decimal_places=2)


class DailyAsset(BaseModel):
    id = PrimaryKeyField()
    account = ForeignKeyField(Account)
    currency = CharField(20)
    date = DateField()
    total_market_value = DecimalField(decimal_places=2)

db.connect()
db.create_tables([Price, TradingDate, StockInfo, Account, OrderInfo, Position, DailyAsset, Cash, Settlement], safe=True)
