class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(len(stones)):
            stones[i]*=-1
        heapq.heapify(stones)

        while stones :
            first = heapq.heappop(stones)
            if not stones:
                return -1*first
            second = heapq.heappop(stones)
            if first != second:
                heapq.heappush(stones ,first - second)
        
        return 0
            

        