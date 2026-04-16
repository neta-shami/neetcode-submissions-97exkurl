class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def color(i,j):
            if i<0 or i>=n or j<0 or j>=m or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for x,y in directions:
                color(i+x, y+j)
                

        islands = 0
        n = len(grid)
        m = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    islands+=1
                    color(i,j)
        
        return islands
        
        
            

