class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m= len(heights)
        n= len(heights[0])
        pacific = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        
        for i in range(m):
            pacific.add((i,0))
            q.append((i,0))

        for j in range(1,n):
            pacific.add((0,j))
            q.append((0,j))
        
        while q:
            (i , j) = q.popleft()
            for x , y in directions:
                ni, nj = i+x , j+y
                if 0<=ni<m and 0<=nj<n and (ni,nj) not in pacific and heights[i][j] <= heights[ni][nj]:
                    pacific.add((ni ,nj))
                    q.append((ni,nj))
                
        atlantic = set()
        q = deque()
        
        for i in range(m):
            atlantic.add((i,n-1))
            q.append((i,n-1))

        for j in range(n-1):
            atlantic.add((m-1,j))
            q.append((m-1,j))
        
        while q:
            (i , j) = q.popleft()
            for x , y in directions:
                ni, nj = i+x , j+y
                if 0<=ni<m and 0<=nj<n and (ni,nj) not in atlantic and heights[i][j] <= heights[ni][nj]:
                    atlantic.add((ni ,nj))
                    q.append((ni,nj))
        
        result = []
        for item in atlantic:
            if item in pacific:
                result.append(list(item))
        return result
    
                




            

        