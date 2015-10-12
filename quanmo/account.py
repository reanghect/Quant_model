class Account(object):

	def __init__(self, sim_params = None,strg = None, data_all = None, commission = Commission()):
		self.sim_params =  sim_params 	# Backtesting Parameter
		self.universe_all =   	# Stock_pool_all
		self.universe =   		# Stock poll based on everyday
		self.current_date = 	# current date
		self.days_counter = 	# counting the trading day
		self.trading_days = 	# All the trading day list in backtesting
		self.position = 		# cash and security position
		self.cash = 			# cash position
		self.secpos = 			# security position,dic, key=stock_code, value=position
		self.avail_secpos = 	# securities available to sell
		self.referencePrice = 	# reference price: closing price in lastday
		self.referenceReturn = 	# reference return: return in last day
		self.blotter = 			# bid-ask list
		self.commission = commission		# commission standard

	def handle_data(self,data): 
		# execute strg.handle_data(self.data)
		# execute transact(self.data)
		# judge self.blotter
		# update self.blotter and self.position

	def __get_daily_symbol_history(self,symbol, time_range):
		# get daily history on given stock
		# time_range(int) return list or dict
		return get_daily_symbol_history

	def __get_daily_att_history(self, attribute, time_range):
		# get daily attribute
		return 

	def __get_daily_history(self, time_range):
		# get daily history of all stocks

	def __referencePrice(self):
		# get reference price: last closing price

		# return self.universe stock price(dict)
	def __referenceReturn(self):
		# get reference return: last day return

		# return self.universe stock price(dict)


