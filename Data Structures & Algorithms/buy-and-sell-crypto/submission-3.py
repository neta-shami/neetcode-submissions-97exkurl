class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy , sell = 0,1
        maxProfit = 0

        while sell <len(prices):
            if prices[buy] < prices[sell]:  #we have profit
                if prices[sell-1] < prices[sell]: #better profit
                    profit = prices[sell] - prices[buy]
                    maxProfit = max(maxProfit , profit)
            else: #we fount lower change to buy 
                buy = sell
            sell+=1 # as long as we didn't find better time to buy we keep scaninng for time to sell 
        return maxProfit
