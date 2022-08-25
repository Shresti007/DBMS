class Stack:
    def __init__(self, limit = 10):
        self.stk = limit*[None]
        self.limit = limit

    def isEmpty(self):
        return len(self.stk) <= 0

    def push(self, item):
        if len(self.stk) >= self.limit:
            self.resize()
        self.stk.append(item)
        print(self.stk, "push over")

    def pop(self):
        if len(self.stk) <= 0:
            return "Stack is Underflow"
        else:
            return self.stk.pop()

    def peek(self):
        if len(self.stk) <= 0:
            return "stack underflow"
        else:
            return self.stk[-1]

    def size(self):
        return len(self.stk)

    def resize(self):
        new_stk = list(self.stk)
        self.limit = 2*self.limit
        self.stk = new_stk

stack = Stack(3)
stack.isEmpty()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.pop()
stack.peek()
stack.size()
stack.isEmpty()





