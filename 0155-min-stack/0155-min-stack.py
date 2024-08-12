class MinStack:

    def __init__(self):
        self.st = []
        self.minEle = None

    def push(self, val: int) -> None:
        if not self.st:
            self.minEle = val
            self.st.append(val)
        else:
            if val >= self.minEle:
                self.st.append(val)
            else:
                self.st.append(2 * val - self.minEle)
                self.minEle = val

    def pop(self) -> None:
        if not self.st:
            return
        top = self.st.pop()
        if top < self.minEle:
            self.minEle = 2 * self.minEle - top

    def top(self) -> int:
        if not self.st:
            return -1
        top = self.st[-1]
        if top >= self.minEle:
            return top
        else:
            return self.minEle

    def getMin(self) -> int:
        return self.minEle



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()