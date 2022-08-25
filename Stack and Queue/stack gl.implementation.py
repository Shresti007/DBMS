# through arr
class Stack:

    def __init__(self, maxsize):
        self.stack = []                  # it is arr where we store items
        self.maxsize = maxsize
        self.top = -1    # which shows ur top is empty as of start

    def push(self, item):
        if self.top == self.maxsize-1:    # it shows whether we crossed overflow condition
            print("overflow: stack is full")
            return
        self.stack.append(item)
        print(item, "is pushed.")
        self.top += 1

    def isEmpty(self):
        if self.top == -1:
            return True
        return False

    def peek(self,):
        return self.stack[self.top]

    def stackSize(self):
        ''' Returns the current stack size '''
        return len(self.stack)

    def pop(self):
        return self.stack.pop()



stack = Stack(3)
print(stack.isEmpty())
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
print(stack.peek())
print(stack.pop())
stack.push(7)
stack.push(8)
stack.push(9)
print(stack.stackSize())
print(stack.stack)
