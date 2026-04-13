class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxArea = max(heights)
        n = len(heights)

        for i in range(n):
            minH = heights[i]
            for j in range(i+1,n):
                minH = min(heights[j] , minH)
                area = minH*(j-i+1)
                maxArea = max(maxArea,area)

        return maxArea



        