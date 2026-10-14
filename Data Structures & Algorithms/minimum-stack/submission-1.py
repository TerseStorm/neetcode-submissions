class MinStack:

    def __init__(self):
        self.stack = []
        # Makes sense
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack and val <= self.minStack[-1]:
            self.minStack.append(val)
        elif len(self.minStack) == 0:
            self.minStack.append(val)
        

    def pop(self) -> None:
        top = self.stack[-1]
        self.stack.pop()
        if self.minStack and self.minStack[-1] == top:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
