class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)    #number of row - len of col
        m = len(matrix[0]) #number of col - len of row

        if matrix[0][0] > target:
            return False
        
        #search for upper bound in col 0 (so we know which row its in)
        l, r = 0, n

        while l < r:
            mid = l + ((r - l) // 2)
            if matrix[mid][0] > target:
                r = mid
            elif matrix[mid][0] <= target:
                l = mid + 1
        
        #after this loop l is pointing to the row next to target 
        possibleRow=l-1

        l, r = 0, m-1

        while l <= r:
            mid = l + ((r - l) // 2)
            if matrix[possibleRow][mid] > target:
                r = mid-1
            elif matrix[possibleRow][mid] < target:
                l = mid + 1
            else:
                return True
        
        return False


        
        

        

        
        