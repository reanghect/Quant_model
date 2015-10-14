def stock_scan(Index):
	if Index = 'HS300':
		### Symbol_list = Get list of HS300
		for s in Symbol_list:
			del s if s.match('ST')
	elif Index = 'A':
		### Symbol_list = Get list of A
		for s in Symbol_list:
			del s if s.match('ST')
	else:
		### Symbol_list = Get list of SH180
		for s in Symbol_list:
			del s if s.match('ST')
	return Symbol_list

def closing_price(date,symbol):
	# getting closing_price of given stock list in a given day, return dict
	# for l in symbol:
	# 	pass

	return ['symbol': 'closing_price']

def Trading_day(start, end):
	# getting trading calender between start and end, return date list of trading day

	return datelist

def strategy(date, factor):

def commission(amount):
	if amount >0:
		return 0.001
	else:
		return -0.002
