class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        num1 , num2 = 0,0

        for c in cost:
            num3 = min(num1+c , num2+c)
            num1 , num2 = num2 , num3

        return min(num1 ,num2)

        