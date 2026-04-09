import heapq

#This has another solution that is better time complexity 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        elementToCount = defaultdict(int)
        maxHeap =  []
        
        #create dict of (val , count) O(n)
        for element in nums:
            elementToCount[str(element)] +=1
        
        
        # create dict of count val - possible beacuse its unique O(n)
        for val in elementToCount.keys():
            value = int(val)
            countOfValue = elementToCount.get(val) * -1  #for max heap
            maxHeap.append( tuple([countOfValue , value]))

        heapq.heapify(maxHeap)

        # get K elements (counts) k*log n
        result = []   
        for _ in range(k):
            ( _ , val )  = heapq.heappop(maxHeap)
            result.append(val)
        
        return result

