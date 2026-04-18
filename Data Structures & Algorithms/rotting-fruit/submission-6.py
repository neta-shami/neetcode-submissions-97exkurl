class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        visited = set()
        q = deque()
        fresh = 0
        

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh +=1
                elif grid[i][j] == 2:
                    q.append((i,j))
                    visited.add((i,j))
        
        if fresh == 0:
            return 0
        time = 0
        directions = [(1,0) , (-1,0) , (0,1) , (0,-1)]
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                for x,y in directions:
                    ni , nj = i+x , j+y
                    if ni>=0 and nj>=0 and ni<m and nj<n and (ni,nj) not in visited and grid[ni][nj] == 1:
                        fresh-=1
                        q.append((ni,nj))
                        visited.add((ni,nj))
            time+=1
        
        if fresh == 0:
            return time-1
        return -1


        
