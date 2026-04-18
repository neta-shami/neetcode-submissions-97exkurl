class Solution:
    def hammingWeight(self, n: int) -> int:
        
        mask = 1
        count = 0
        while n > 0:
            count += (mask&n)
            n >>= 1
        return count
            

        