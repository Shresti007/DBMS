class ArrayStack:

    def __init__(self):
        self._stk = []  # _data we are using because in python we do not have arrays and so we use lists to
        # implement stacks using array

    def __len(self):
        return len(self._stk)

    def isEmpty(self):
        return len(self._stk) == 0

    def push(self, data):
        self._stk.append(data)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self._stk.pop()

    def peek(self):  # remember in python u can have positive as welll as neg as index num  -1 indicates last
        # element of list
        if self.isEmpty():
            return "stack is empty"
        return self._stk[-1]
