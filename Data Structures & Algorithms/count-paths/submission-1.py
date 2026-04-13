class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        prevRow = [1]*n
        nextRow = [1]*n

        for _ in range(1,m):
            prevRow = nextRow
            nextRow[0] = 1
            for col in range(1,n):
                nextRow[col] = nextRow[col-1] + prevRow[col]

        
        return nextRow[n-1]

            

        