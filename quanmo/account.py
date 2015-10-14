class Account(object):

	referencePrice = fc.closing_price(preTradeDate,universe)						# reference price: closing price in lastday
	Total_market_value = sum([referencePrice[l] * position[l] for l in universe])

	def __init__(self, start, universe, capital_base):
		
		self.date =  start 								# Backtesting date
		self.universe =  fc.stock_scan(universe) 		# Stock poll based on everyday
		self.cash = capital_base						# cash position
		self.position = []								# security position,dic, key=stock_code, amount=position
		self.avail_secpos = []							# securities available to sell,dict

	def order(date, amount, symbol):

		deal_price = fc.closing_price(date,symbol) + fc.commission(amount) #closing price, matrix in numpy

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


	def transact(date,preTradeDate):
		# update position available position and cash
		# return daily position

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


