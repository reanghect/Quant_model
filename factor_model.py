# ! /usr/lib/env python
# -*- coding: utf-8 -*-


import numpy as np, scipy as sp, pandas as pd, matplotlib as mpl
import backtest as bt,account as ac, func as fc

start =  '2014-01-01'						# start date
end = '2015-08-31'							# end date
benchmark = 'HS300'							# Select index as benchmark

######### Loading data ####### 

##############################

universe = fc.stock_scan('HS300')			# stock pool (list)
capital_base = 100000						# starting capital
fre  = 'd'									# trading frequency


accounts = ac.Account(start, universe, capital_base)

Test_report = bt.backtest(start, end, accounts, factor)

performance(Test_report)