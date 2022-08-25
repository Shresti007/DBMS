# from exceptions import Empty


class LinkedStack:
    class _Node:                        # passing inner class Node
        __slots__ = '_data', '_next'

        def __init__(self, data, next):
            self._data = data
            self._next = next

    def __init__(self):
        self._top = None
        self._size = 0     # limit parameter i think so

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, data):
        self._top = self._Node(data, self._top)  # here self.top is used as reference
        self._size = self._size+1   # incrementing the stack

    def pop(self):     # it is one of the stack adt
        if self.is_empty():
            raise Empty("Stack is Empty")  # using exceptions class
        value = self._top._data   # followed by above pop method
        self._top = self._top._next
        self._size = self._size - 1  # decrement value as poped out from stack
        return value                 # return the poped element to view

    def peek(self):
        if self.is_empty():
            raise Empty(" Stack is empty")
        return self._top._data

    def display(self):
        temp = self._top   # to display or print an element we have to send them by creating temp ll
        while temp:
            print(temp._data, end ='-->')
            temp = temp._next
        print()


ls = LinkedStack()
ls.push(10)
ls.push(30)
ls.push(40)
ls.push(50)
ls.push(60)
ls.display()
print('Popped: ', ls.pop())
ls.display()
ls.push(70)
print('Top Element: ', ls.pop())
print('Popped: ', ls.pop())
ls.display()


