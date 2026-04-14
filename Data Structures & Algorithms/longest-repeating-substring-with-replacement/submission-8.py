class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)

        if n==1:
            return 1

        counter = defaultdict(int)
        maxLen = 0
        i , j = 0,0

        while j<n:
            counter[s[j]] +=1
            m = getMaxLetter(counter)
            if j-i+1-m > k: 
                maxLen= max(j-i, maxLen)
                counter[s[i]] -=1
                i+=1
            j+=1
        
        maxLen= max(j-i , maxLen)    
        return maxLen

def getMaxLetter(counter):
    m = 0
    for i in counter:
        m = max(m , counter[i])
    return m
            

        