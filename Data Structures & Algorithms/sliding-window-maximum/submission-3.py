import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 1:
            return nums
        if k == n:
            return [max(nums)]
        
        result = []
        
        j=0
        heap = []
        while j < k: 
            heap.append(tuple([-1*nums[j], j]) )
            j+=1
        heapq.heapify(heap) #O(K) 
        result.append(-1*heap[0][0])

        while j< n:
            heapq.heappush(heap , tuple([-1*nums[j], j])) 
            while heap[0][1] < j+1-k: #num not in range
                heapq.heappop(heap)
            result.append(-1*heap[0][0])
            j+=1
        return result





        