class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        if n ==0 : 
            return 0
  
        
        seen = set()
        maxLen = 1
        start , end = 0,0

        while end<n:
            if s[end] not in seen:
                seen.add(s[end])
                maxLen = max(maxLen , (end-start+1))
            else:
                while start<end and s[start]!=s[end]:
                    seen.remove(s[start])
                    start+=1
                start+=1
            end+=1
        
        return maxLen

