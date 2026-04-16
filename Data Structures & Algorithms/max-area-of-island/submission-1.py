class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxArea = 0
        n = len(grid)
        m = len(grid[0])
        directions = [ (1,0), (-1,0), (0,1), (0,-1) ]
        
        def bfs(i ,j):
            
            q = collections.deque()
            grid[i][j] = 0
            area = 1
            q.append((i,j))
            
            while q:
                i,j = q.popleft()
                for x , y in directions:
                    ni , nj = i+x, y+j
                    if ni>=0 and nj>=0 and ni<n and nj<m and grid[ni][nj] == 1: 
                        grid[ni][nj] = 0
                        q.append((ni,nj))
                        area += 1
            
            return area

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = bfs(i , j)
                    maxArea = max(maxArea , area)
        return maxArea
        
                
                            

            
            

                
