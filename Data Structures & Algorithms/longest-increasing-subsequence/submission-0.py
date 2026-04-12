class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n

        for i in range(n-2 , -1 , -1):
            j = i+1
            maxL = 1
            while j<len(nums):
                if nums[i] < nums[j]:
                    maxL = max(maxL , dp[j]+1)
                j+=1

            dp[i] = maxL
        
        return max(dp)

        