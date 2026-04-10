class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        leftToRight = []
        rightToLeft = []

        totalProoduct = 1
        for num in nums:
            totalProoduct *= num 
            leftToRight.append(totalProoduct)
   
        totalProoduct = 1
        for num in nums[::-1]:
            totalProoduct *= num 
            rightToLeft.append(totalProoduct)
        rightToLeft = rightToLeft[::-1]

        
        result = []
        for i , num in enumerate(nums):
            if i == 0:
                result.append(rightToLeft[1])
            elif i == len(nums)-1:
                result.append(leftToRight[len(nums)-2])
            else:
                result.append(leftToRight[i-1] * rightToLeft[i+1])
        return result 

            
        
        
        
        '''
        hasZero = False  # to prevent zero devition 
        totalProduct=1
        for num in nums:
            if num == 0:
                hasZero = True
            else:
                totalProduct*=num
        
        if hasZero == False:
            result = [ totalProduct//num for num in nums]
        else: 
            result = [ totalProduct if num == 0 else 0 for num in nums ]
        
        return result
        '''
        
        