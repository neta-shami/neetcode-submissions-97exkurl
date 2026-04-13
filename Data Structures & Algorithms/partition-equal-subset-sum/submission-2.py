class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        s = sum(nums)
        if s % 2 ==1:
            return False
        
        target = s //2
        memo = [ [-1] * (target+1) for _ in range(len(nums)+1)]
        
        def subsetSum(nums , i , target):
            if target == 0 :
                return True
            if target < 0:
                return False
            if i >= len(nums):
                return False
            if memo[i][target] != -1:
                return memo[i][target]
            
            memo[i][target] = subsetSum(nums , i+1 , target-nums[i]) or subsetSum(nums , i+1 , target)
            return memo[i][target]
        
        return subsetSum(nums , 0 , target)