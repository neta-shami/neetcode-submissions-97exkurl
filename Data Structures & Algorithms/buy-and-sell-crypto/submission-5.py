class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for price in prices[1:]:
            maxP = max(maxP, price - minBuy)
            minBuy = min(minBuy, price)
        return maxP
