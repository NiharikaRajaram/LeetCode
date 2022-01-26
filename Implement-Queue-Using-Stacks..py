class MyQueue:

    def __init__(self):
        self.ins = []
        self.out = []

    def push(self, x: int) -> None:
        self.ins.append(x)
        
    def transfer(self, ins, out):
        while(len(self.ins) != 0):
            out.append(self.ins.pop())

    def pop(self) -> int:
        if(len(self.out) == 0):
            self.transfer(self.ins, self.out)
        return self.out.pop()

    def peek(self) -> int:
        if(len(self.out) == 0):
            self.transfer(self.ins, self.out)
        return self.out[-1]

    def empty(self) -> bool:
        return len(self.ins) == 0 and len(self.out) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
