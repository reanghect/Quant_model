

def backtest(start, end, benchmark, accounts, strategy,fre):
	for date in daterange(start,end):
		portfolio_symbol = strategy(date,'factor')  # Get daily security position symbol (list)
		for symbol in portfolio_symbol:
			amount = total_market_value(last_date)/10/closing_price(symbol, date)
			trading_amount = amount- accounts.position[security]
			accounts.order(trading_amount, symbol)
		position = [symbol: amount]

	# Factor From handle data function: get trading command
	# Order
	# Logger
	# update account
		return Test_report, Test_account
