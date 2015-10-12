class Commission(object):
	def __ini__(self,buycost=0.001, sellcost = 0.002, unit = "perValue")
		self.buycost = buycost
		self.sellcost = sellcost
		slef.unit =	unit

	def calculate(self,price,direction):
		if direction = 1:
			deal_price = price + self.buycost
		else:
			deal_price = price - self.sellcost

		return deal_price
		
