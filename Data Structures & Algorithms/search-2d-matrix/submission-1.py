class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        total = []
        for row in matrix:
            total+=row
        
        l, r = 0 , len(total)-1
        while l<=r:
            mid = (l+r)//2
            if total[mid] == target:
                return True
            elif total[mid] < target:
                l = mid+1
            else:
                r = mid -1
            
        return False

        

        
        