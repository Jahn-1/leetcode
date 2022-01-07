class Solution:
	def maxProfitBrute(self, prices):
		# brute force
		largest_profit = 0
		for idx1, price1 in enumerate(prices):
			for price2 in prices[idx1:]:
				if (price2 - price1 > largest_profit):
					largest_profit = price2 - price1

		return largest_profit

	def maxProfit(self, prices):
     	# questions solution is assuming that the smallest valley and highest trough will ultimatley
		# give you the largest_profit. but this isnt the case. [2,8,1,3] is a case that breaks this.
		# 1 is lower than 2 (valley) and after that there is a 3 making the "largest" (incorrect) profit
		# 2 when it should be 8 - 2. for this reason the algorithim in most simple form must be brute force.
		# have to check every possible solution.
		largest_profit = 0
            
                
        