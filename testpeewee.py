#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from peewee import *

__author__ = 'Will Chen'


db = MySQLDatabase("qss_hist", host="localhost", port=3306, user="qss", passwd="Abc123")


class BaseModel(Model):
    class Meta:
        database = db


class Price(BaseModel):
    id = PrimaryKeyField()
    trading_date = DateField(index=True)
    ticker = CharField(20, index=True)
    exchId = CharField(20)
    high = DecimalField()
    low = DecimalField()
    open = DecimalField()
    close = DecimalField()
    adj_close = DecimalField()
    volume = IntegerField()


class TradingDate(BaseModel):
    id = PrimaryKeyField()
    date = DateField(unique=True)
    isOpen = CharField(20)


db.connect()
db.create_tables([Price])
