class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        s = sum(nums)
        if s % 2 ==1:
            return False
        
        target = s /2

        def subsetSum(nums , i , target):
            if target == 0 :
                return True
            if target < 0:
                return False
            if i >= len(nums):
                return False
            
            return subsetSum(nums , i+1 , target-nums[i]) or subsetSum(nums , i+1 , target)
        
        return subsetSum(nums , 0 , target)