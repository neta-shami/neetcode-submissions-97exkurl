class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        result = [0]*n

        for i in range(n-2 , -1 ,-1):
            j = i+1
            while j<n and temperatures[j] <= temperatures[i]: #j not warmer then i
                if result[j] == 0: #there is not a warmer day
                    j = n+1               #set j = n+1 so in the end we know not to set result
                    break
                
                j+=result[j]  #temperatures[j] <= temperatures[i] so we move j to the next day the is warmer
            
            if j<n:
                result[i] = j-i
        
        return result
        
        
        