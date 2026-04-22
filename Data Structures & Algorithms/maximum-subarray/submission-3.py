class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = max(nums)
        if maxSum<=0:
            return maxSum
            
        maxSum = 0
        currSum = 0
        for num in nums:
            currSum = max(currSum+num , 0)
            maxSum = max(currSum , maxSum)
        return maxSum



        