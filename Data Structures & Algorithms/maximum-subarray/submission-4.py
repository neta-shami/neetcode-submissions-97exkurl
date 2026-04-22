class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSum = 0
        currSum = 0
        maxNum = nums[0]
        for num in nums:
            currSum = max(currSum+num , 0)
            maxSum = max(currSum , maxSum)
            maxNum = max(maxNum , num)
        if maxNum<0:
            return maxNum
        return maxSum



        