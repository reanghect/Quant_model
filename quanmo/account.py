class Account(object):

	position = []
	settlement = []

	def __init__(self, start, end, universe, capital_base, refresh_rate):
		self.sim_params =  sim_params 	# Backtesting Parameter
		self.universe_all =   	# Stock_pool_all
		self.universe =   		# Stock poll based on everyday
		self.current_date = 	# current date
		self.days_counter = 	# counting the trading day
		self.trading_days = 	# All the trading day list in backtesting
		self.position = 		# cash and security position
		self.cash = capital_base			# cash position
		self.secpos = 0			# security position,dic, key=stock_code, value=position
		self.avail_secpos = 0	# securities available to sell
		self.referencePrice = None	# reference price: closing price in lastday
		self.referenceReturn = None	# reference return: return in last day
		self.blotter = None			# bid-ask list
		self.commission = commission		# commission standard


	def order(amount, symbol):

		deal_price = closing_price(data,symbol) + direction * commission #closing price, matrix in numpy

		if amount > 0 && avail_position[symbol] >= amount:
			# log: selling deal
			avail_position[symbol] -= amount
			position[symbol] -=amount
			cash += deal_price * amount
		elif amount < 0 && cash >= deal_price * amount:
			# log: buying deal
			position[symbol] += amount
			cash = cash - deal_price * amount
		else:
			# log: deal failed
			# log: Date + symbol + direction + postion transfer failed
			pass


	def transact(date,last_date):

	# def handle_data(self,data): 
	# 	# execute strg.handle_data(self.data)
	# 	# execute transact(self.data)
	# 	# judge self.blotter
	# 	# update self.blotter and self.position

	# def __get_daily_symbol_history(self,symbol, time_range):
	# 	# get daily history on given stock
	# 	# time_range(int) return list or dict
	# 	return get_daily_symbol_history

	# def __get_daily_att_history(self, attribute, time_range):
	# 	# get daily attribute
	# 	return 

	# def __get_daily_history(self, time_range):
	# 	# get daily history of all stocks

	# def __referencePrice(self):
	# 	# get reference price: last closing price

	# 	# return self.universe stock price(dict)
	# def __referenceReturn(self):
	# 	# get reference return: last day return

	# 	# return self.universe stock price(dict)


