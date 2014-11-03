class Solution:
    # @param prices, a list of integer
    # @return an integer
	def maxProfit(self, prices):
		days = len(prices)
		        
		if days < 2:
			return 0
		            
		buy = prices[0]
		profit = 0
		
		for i in range(1, days):
			profit = max(profit, prices[i] - buy)
			buy = min(buy, prices[i])

		return profit