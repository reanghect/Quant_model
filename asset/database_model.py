#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from peewee import *
import configparser
import os

cf = configparser.ConfigParser()
conf_path = os.path.join(os.path.dirname(__file__), '../conf/database.conf')
cf.read(conf_path)

s = cf.sections()
db_host = cf.get("db", "db_host")
db_port = cf.getint("db", "db_port")
db_user = cf.get("db", "db_user")
db_pass = cf.get("db", "db_pass")


db = MySQLDatabase("QSS", host=db_host, port=db_port, user=db_user, passwd=db_pass)


class BaseModel(Model):
    class Meta:
        database = db


class DailyPrice(BaseModel):
    id = PrimaryKeyField()
    trading_date = DateField()
    ticker = CharField(20)
    market_id = CharField(20)
    high = DecimalField(decimal_places=2, null=True)
    low = DecimalField(decimal_places=2, null=True)
    open = DecimalField(decimal_places=2, null=True)
    close = DecimalField(decimal_places=2, null=True)
    volume = FloatField(null=True)

    # class Meta:
    #     # multiple column index or multiple indexes
    #     indexes = ((('trading_date', 'ticker', 'exchId'), True),)


class IntraPrice(BaseModel):
    id = PrimaryKeyField()
    time = TimeField()
    ticker = CharField(20)
    high = DecimalField(decimal_places=2, null=True)
    low = DecimalField(decimal_places=2, null=True)
    open = DecimalField(decimal_places=2, null=True)
    trade = DecimalField(decimal_places=2, null=True)
    change_percent = DecimalField(decimal_places=2, null=True)
    volume = FloatField(null=True)


class TradingDate(BaseModel):
    id = PrimaryKeyField()
    date = DateField()
    exchangeCD = CharField(20)
    isOpen = BooleanField()
    isMonthEnd = BooleanField()
    isQuarterEnd = BooleanField()
    isWeekEnd = BooleanField()
    isYearEnd = BooleanField()
    prevTradeDate = DateField()


class StockInfo(BaseModel):
    id = PrimaryKeyField()
    ticker = CharField(20, unique=True)
    market_id = CharField(20)
    exchangeCD = CharField(20)
    asset_class = CharField(20)
    short_name = CharField(50, unique=True)
    currency = CharField(10)
    sector = CharField(20)

    # class Meta:
    #     indexes = ((('ticker', 'market_id'), True),)


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


class TechIndicator(BaseModel):
    id = PrimaryKeyField()
    trading_date = DateField()
    ticker = CharField(20)
    shortSMA = DecimalField(decimal_places=2, null=True)
    longSMA = DecimalField(decimal_places=2, null=True)
    MACD = DecimalField(decimal_places=2, null=True)


def create_tables():
    db.connect()
    db.create_tables([DailyPrice, IntraPrice, TradingDate, StockInfo, Account, OrderInfo, Position, DailyAsset,
                      Cash, Settlement, TechIndicator], True)
    db.close()


def drop_tables():
    db.connect()
    db.drop_tables([DailyPrice, IntraPrice, TradingDate, StockInfo, Account, OrderInfo, Position, DailyAsset,
                    Cash, Settlement, TechIndicator], True)
    db.close()
