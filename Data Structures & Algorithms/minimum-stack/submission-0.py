class MinStack:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self, value: int) -> None:
        self.stack1.append(value)
        if not self.stack2:
            self.stack2.append(value)
        else:
            if value <= self.stack2[-1]:
                self.stack2.append(value)

    def pop(self) -> None:
        if self.stack1:
            if self.stack1[-1] == self.stack2[-1]:
                self.stack1.pop()
                self.stack2.pop()
            else:
                self.stack1.pop()

    def top(self) -> int:
        if self.stack1:
            return self.stack1[-1]

    def getMin(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()