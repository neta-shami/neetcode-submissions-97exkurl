class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens) == 1 or len(tokens) == 2:
            return int(tokens[0])
        
        stack = []
        
        for token in tokens:
            if token in ["+" , "-" , "*" , "/"]:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(operate(token , num1 , num2))
            else:
                stack.append(int(token))
        
        return stack.pop()

        
def operate(operator, num1 , num2):
        if operator == "+":
            return num1+num2
        elif operator == "-":
            return num1-num2
        elif operator == "*":
            return num1*num2
        else:
            return int(num1/num2)
    