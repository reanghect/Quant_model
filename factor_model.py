# ! /usr/lib/env python
# -*- coding: utf-8 -*-


import numpy as np, scipy as sp, pandas as pd

start =  '2014-01-01'						# start date
end = '2015-08-31'							# end date
benchmark = 'HS300'								# Select index as benchmark
universe = stock_scan()						# stock pool
capital_base = 100000						# starting capital
fre  = 'd'									# trading frequency
refresh_rate = 1

def initialize(account):
	pass

def handle_data(account):
	return