class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t)>len(s):
            return ""
        if s ==t:
            return s
        
        matches =0
        minLen=len(s)+1
        counter = defaultdict(int)
        
        for ch in t:
            counter[ch] +=1
        
        i,j = 0,0
        matchesNeeded = len(counter)

        while j<len(s):
            while j<len(s) and matches<matchesNeeded:
                if s[j] in counter:
                    counter[s[j]]-=1
                    if counter[s[j]] ==0:
                        matches+=1
                j+=1
            while matches == matchesNeeded:
                if s[i] in counter:
                    counter[s[i]]+=1
                    if counter[s[i]] >0:
                        matches-=1
                        if j-i < minLen:
                            startIndex = i 
                            endIndex = j
                            minLen = j-i
                i+=1
        
        if minLen == len(s)+1:
            return ''
        else :
            return s[startIndex:endIndex]
        

                
                
            

