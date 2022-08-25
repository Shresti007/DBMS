"""
 stack can be implemented using two queues. Let stack to be implemented be ‘s’ and queues used to implement be ‘q1’ and
 ‘q2’. Stack ‘s’ can be implemented in two ways:

Method 1 (By making push operation costly)
This method makes sure that newly entered element is always at the front of ‘q1’, so that pop operation just dequeues
 from ‘q1’. ‘q2’ is used to put every new element at front of ‘q1’.

push(s, x) operation’s step are described below:
Enqueue x to q2
One by one dequeue everything from q1 and enqueue to q2.
Swap the names of q1 and q2
pop(s) operation’s function are described below:
Dequeue an item from q1 and return it.
Below is the implementation of the above approach:
"""
# Program to implement a stack using
# two queue
from queue import Queue


class Stack:

    def __init__(self):

        # Two inbuilt queues
        self.q1 = Queue()
        self.q2 = Queue()

        # To maintain current number
        # of elements
        self.curr_size = 0

    def push(self, x):
        self.curr_size += 1

        # Push x first in empty q2
        self.q2.put(x)

        # Push all the remaining
        # elements in q1 to q2.
        while (not self.q1.empty()):
            self.q2.put(self.q1.queue[0])
            self.q1.get()

        # swap the names of two queues
        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q

    def pop(self):

        # if no elements are there in q1
        if (self.q1.empty()):
            return
        self.q1.get()
        self.curr_size -= 1

    def top(self):
        if (self.q1.empty()):
            return -1
        return self.q1.queue[0]

    def size(self):
        return self.curr_size


# Driver Code
if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print("current size: ", s.size())
    print(s.top())
    s.pop()
    print(s.top())
    s.pop()
    print(s.top())

    print("current size: ", s.size())

# This code is contributed by PranchalK


