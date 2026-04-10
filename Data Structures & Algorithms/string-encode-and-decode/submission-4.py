class Solution:

    def encode(self, strs: List[str]) -> str:

        result =""
        for s in strs:
            result += f'#{len(s)}#{s}'

        return result
        


    def decode(self, s: str) -> List[str]:
        
        result = []
        start = 1 # zero points to '#'
        i=1

        while start < len(s):
            #Find closing '#'
            while s[i]!= '#':
                i+=1

            wordLen = int(s[start : i])
            #move i to the start of the word
            i+=1
            word = s[i : i+wordLen]
            result.append(word)
            #move start after the next '#'
            start = i+wordLen+1
            #move i to start
            i = start
        
        return result
