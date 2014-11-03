class Solution:
	# @param prices, a list of integer
	# @return an integer
	def maxProfit(self, prices):
		days = len(prices)
		if days < 2:
			return 0
		profit = 0
		buyDay = 0
		sellDay = 1
		while sellDay < days and buyDay < days - 1:
			while sellDay < days - 1 and prices[sellDay + 1] >= prices[sellDay]:
				sellDay = sellDay + 1
			while buyDay + 1 < sellDay and prices[buyDay + 1] <= prices[buyDay]:
				buyDay = buyDay + 1
			# print buyDay
			# print sellDay
			profitUnit = prices[sellDay] - prices[buyDay]
			if profitUnit > 0:
				profit = profit + profitUnit
			buyDay = sellDay + 1
			sellDay = buyDay + 1
		if profit > 0:
			return profit
		else:
			return 0