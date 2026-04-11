class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if self.stack:
            self.minStack.append(min(self.minStack[-1] , val))
            self.stack.append(val)
        else:
            self.stack.append(val)
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.stack:
            return self.minStack[-1]
        
