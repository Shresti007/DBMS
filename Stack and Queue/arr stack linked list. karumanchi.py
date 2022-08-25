# Node of a Single object.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = next

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next is not None


class LinkedList:
    def __init__(self, data = None):
        self.head = None
        if data:
            for data in data:
                self.push(data)

    def push(self, data):
        new_node = Node(data)
        new_node.set_data(data)
        new_node.set_next(self.head)
        self.head = new_node

    def pop(self):
        if self.head is None:
            raise IndexError
        new_node = self.head.getData()
        self.head = self.head.get_next()
        return new_node

    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.getData()

our_list = ("first", "second", "third", "fourth"!
our_stack = Stack(our_list)
print our stack.pop()
print our stack.pop()


