class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #we can't count to an array becuse -10^9 <= nums[i] <= 10^9 (like bucket sort)
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1


        numbers = set(nums)
        currentLen = 0
        maxLen = 1
        for num in nums:
            
            if num in numbers:
                currentLen = 0
                start = num
                # find the start of the sequence
                while start-1 in numbers:   #max O(n)
                    start-=1
                
                while start in numbers:     #max O(n)
                    currentLen+=1
                    numbers.remove(start)
                    start+=1
                
                maxLen = max(maxLen , currentLen)
        return maxLen



        