class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l , r = 1,max(piles)
        
        while l<r:
            mid = (l+r)//2
            time1 = 0
            for pile in piles:
                time1+= -(-pile // mid)
            print(f' l {l} , r {r} , mid {mid} , time {time1}')
            if time1>h:
                l = mid +1
            elif time1 <= h :
                r = mid
            
        return l
            
            
            


        