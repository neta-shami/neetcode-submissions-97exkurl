class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [nums[0]]

        for i in range(1 , n):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                #find lower bound in df (the first number that is bigger or equal to nums[i])
                l,r = 0,len(dp)

                while l<r:
                    mid = (l+r)//2
                    if dp[mid] >= nums[i]:
                        r = mid
                    else:
                        l = mid +1
                #the lower bount is l-1
                dp[l] = nums[i]
          
        
        return len(dp)

        