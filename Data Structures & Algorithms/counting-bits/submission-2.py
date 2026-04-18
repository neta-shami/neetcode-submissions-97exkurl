class Solution:
    def countBits(self, n: int) -> List[int]:
        
        result = [0]
        
        for i in range(1,n+1):
            count = 0
            while i>0:
                count+= i&1
                i>>=1
            result.append(count)
        return result
        