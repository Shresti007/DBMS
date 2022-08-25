class Stack:
    def __init__(self, limit):
        self.stk = []
        self.limit = limit

    def isEmpty(self):
        return len(self.stk) <= 0

    def push(self, item):
        if len(self.stk) >= self.limit:
            print("stk overflow")
        else:
            self.stk.append(item)
        print(self.stk,"after pushed")

    def pop(self):
        if len(self.stk) <= 0:
            print("stk under flow")
        else:
            return self.stk.pop()

    def peck(self):
        if len(self.stk) <= 0:
            print("Stack underflow")
            return 0
        else:
            return self.stk[-1]    # it states exhbit top element

    def size(self):
        return len(self.stk)


stack = Stack(3)
print(stack.isEmpty())
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
stack.push(9)
print(stack.pop())
print(stack.peck())
print(stack.size())