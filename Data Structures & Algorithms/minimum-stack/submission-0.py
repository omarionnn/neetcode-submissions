class MinStack:

    def __init__(self):
        self.cont = []
        

    def push(self, val: int) -> None:
        self.cont.append(val)
        

    def pop(self) -> None:
        self.cont.pop()
        

    def top(self) -> int:
        return self.cont[-1]
        

    def getMin(self) -> int:
        return min(self.cont)
        
