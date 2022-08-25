class Stack:
    # We use a basic list to implement a Stack data structure
    def __init__(self):
        self._stack = []

    # Returns true if the stack is empty
    def empty(self):
        # Implement the logic and remove 'pass'
        if len(self._stack) <= 0:                       # check the stack is empty or what
            return True

    # Returns the length of the stack
    def size(self):
        # Implement the logic and remove 'pass'
        return len(self._stack)                         # measuring the size of stack using len method

    # Pushes elements on the stack by appending to the end of the list
    def push(self, item):
        # Implement the logic and remove 'pass'
        self._stack.append(item)                        # piling up the songs played to stack

    # Removes the last items in the list, and returns it.
    # It returns None if the stack is empty
    def pop(self):
        # Implement the logic and remove 'pass'
        if not self.empty():                            # checking the emptiness of song
            return self._stack.pop( )                   # deleting songs from stack
        return None

    # Returns the top of stack without removing it from the stack
    # Sometimes you need to peek at the value but not remove it from the stack yet
    # It returns None if the stack is empty
    def peek(self):
        if not self.empty() :                           # condition if stack not empty
            return self._stack[-1]                      # return the top most song
        else :
            return None


