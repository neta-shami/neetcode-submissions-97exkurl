class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)

        if n==1:
            return 1

        counter = defaultdict(int)
        maxLen = 0
        i , j = 0,0
        currLetter = s[i]

        while j<n:
            counter[s[j]] +=1
            m = getMaxLetter(counter)
            if j-i+1-m > k: 
                maxLen= max(j-i, maxLen)
                while s[i] == currLetter:
                    counter[s[i]] -=1
                    i+=1
                currLetter = s[i]
            j+=1
        
        maxLen= max(j-i , maxLen)    
        
        counter = defaultdict(int)
        i , j = n-1, n-1
        currLetter = s[i]
        
        while j>=0:
            counter[s[j]] +=1
            if i-j+1-getMaxLetter(counter) > k: #skips<= k
                maxLen= max(i-j, maxLen)
                while s[i] == currLetter:
                    counter[s[i]] -=1
                    i-=1
                currLetter = s[i]
            j-=1
        
        maxLen= max(i-j , maxLen)  
        
        return maxLen

def getMaxLetter(counter):
    m = 0
    for i in counter:
        m = max(m , counter[i])
    return m


            

        