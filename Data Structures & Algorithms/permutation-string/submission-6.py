class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        letters1 = defaultdict(int)
        for c in s1:
            letters1[c]+=1
      
        i, j= 0,0
        while i<len(s2):
            while j<len(s2) and letters1[s2[j]] >0:
                letters1[s2[j]]-=1
                j+=1
                if j-i == len(s1):
                    return True
            else:
                if i!= j:
                    letters1[s2[i]]+=1
                else:
                    j+=1
            i +=1
            
        return False





        