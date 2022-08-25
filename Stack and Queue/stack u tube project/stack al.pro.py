from exception import Empty


class ArrayStack:   #Softlect u tube

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
            return Empty("Stack is empty")
        return self._stk.pop()

    def peek(self):  # remember in python u can have positive as welll as neg as index num  -1 indicates last
        # element of list
        if self.isEmpty():
            return Empty("stack is empty")
        return self._stk[-1]

    @property
    def stk(self):
        return self._stk


s = ArrayStack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print('Stack: ', s.stk)   # here it is using s._stk as above in property
print('length: ', len(s.stk))
print('Is-Empty: ', s.isEmpty())
print('Stack: ', s.pop())
print('Stack: ', s.stk)   # we are asking to display content of stack
print('Stack: ', s.pop())
print('Is-Empty: ', s.isEmpty())
print('Stack: ', s.stk)   # we are asking to display content of stack
s.push(50)
s.push(60)
print('Top Element: ', s.peek())
print('Stack: ', s.stk)   # we are asking to display content of stack


