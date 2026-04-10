class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        if nums[0] > 0 or nums[-1] < 0:
            return []
        
        for i , num in enumerate(nums):
            twoNumbers = twoSum(nums , -num , i+1 , len(nums)-1)
            for pair in twoNumbers:
                num1 , num2 = pair
                result.add(tuple([num , num1 , num2]))
            

        final = [list(s) for s in result]
        return final

def twoSum(numbers: List[int], target: int ,low , high):

        result = set()
        if len(numbers)<2:
            return []

        while low < high:
            s = numbers[low] +numbers[high]
            if s == target:
                result.add( tuple([numbers[low] , numbers[high]]))
                low+=1
                high-=1
            elif s < target :
                low+=1
            else:
                high-=1
        
        return result