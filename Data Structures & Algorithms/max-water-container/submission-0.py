class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #Brute Force

        n = len(heights)
        maxArea = 0
        for start in range(n-1):
            for end in range(start+1 , n):
                area = (end - start)* min(heights[end] ,heights[start] )
                maxArea = max(area , maxArea)
        
        return maxArea
        