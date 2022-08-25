class SNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        new_node = SNode(data)
        new_node.next = self.top
        self.top = new_node
        print(data, "is pushed." )

    def display(self):
        tmp = self.top   # tmp node to hold our top node
        while tmp is not None:
            print(tmp.data, "-->", end = " ")
            tmp = tmp.next

    def isEmpty(self):
        if self.top is None:
            return True
        return False

    def peek(self):
        if self.top is None:
            raise IndexError
        return self.top

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.top

stack = Stack()
print(stack.isEmpty())
print(stack.peek())
print(stack.pop())
stack.push(10)
stack.push(20)
stack.push(50)
stack.push(60)
stack.display()


