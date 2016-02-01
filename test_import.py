#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import tushare as ts

__author__ = 'Will Chen'


hist = ts.get_hist_data(code='0000063', start='2015-01-01', end='2016-01-01')
