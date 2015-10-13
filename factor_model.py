# ! /usr/lib/env python
# -*- coding: utf-8 -*-


import numpy as np, scipy as sp, pandas as pd, matplotlib as mpl
import backtest as bt,account as ac, 

start =  '2014-01-01'						# start date
end = '2015-08-31'							# end date
benchmark = 'HS300'							# Select index as benchmark
universe = stock_scan('HS300')				# stock pool
capital_base = 100000						# starting capital
fre  = 'd'									# trading frequency
refresh_rate = 1

accounts = ac.Account(start, universe, capital_base, refresh_rate)

Test_report = backtest(start, end, benchmark, accounts, strategy,fre)

performance(Test_report)