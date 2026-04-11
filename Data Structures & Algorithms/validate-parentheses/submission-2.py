class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closeToOpenMap = {
            "}" : "{" ,
            ")" : "(" ,
            "]" : "["
        }

        for ch in s:
            if ch in closeToOpenMap.values(): #if ch is openning  bracket push to stack
                stack.append(ch)
            else:
                if stack and closeToOpenMap[ch] == stack[-1]: #stack is not empty and the openning for ch is in the to-p of the satck
                    stack.pop()
                else:
                    return False 
        
        return len(stack) == 0
        

            




