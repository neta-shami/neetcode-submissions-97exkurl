class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #using set Time: O(n) space: O(n)

        #Soring inplace Time:O(nlogn) , space: O(1) - modify arr

        #value to index : Time O(n) , space: O(1) - modify arr

        n = len(nums) - 1

        for i , num in enumerate(nums):
            if num -1 == i: # the number is in the right cell
                pass
            else:
                if nums[num-1] == num :
                    return num
                #switch 
                temp = nums[num-1]
                nums[num-1] = num
                nums[i] = temp
        
        return num