class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l , r = 1,max(piles)
        
        while l<r:
            mid = (l+r)//2
            time1 = 0
            for pile in piles:
                time1+= -(-pile // mid)
            if time1>h:
                l = mid +1
            else:
                r = mid
            
        return l
            
            
            


        