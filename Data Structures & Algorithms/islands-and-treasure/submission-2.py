class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        m = len(grid)
        n = len(grid[0])
        directions = [(1,0) , (-1,0) , (0,1) ,(0,-1)]

        def dfs( i , j , level):
            for x , y in directions:
                ni, nj = i+x , j+y
                if ni>=0 and nj>=0 and ni<m and nj<n and grid[ni][nj]>level:
                    grid[ni][nj] = level
                    dfs( ni , nj , level+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i,j ,1)
        
        
        

        