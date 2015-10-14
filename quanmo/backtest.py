

def backtest(start, end, accounts, factor):
	for date in fc. Trading_day(start,end):
		portfolio_symbol = fc.strategy(date,factor)  # Get daily security position symbol (list)
		for symbol in portfolio_symbol:
			amount = total_market_value(preTradeDate)/10/closing_price(symbol, date)
			trading_amount = amount- accounts.position[security]
			accounts.order(date, trading_amount, symbol)
			Test_report = accounts.transact(date, preTradeDate)
		return Test_report
