"""
https://www.geeksforgeeks.org/queue-using-stacks/
While stack1 is not empty, push everything from stack1 to stack2.
Push x to stack1 (assuming size of stacks is unlimited).
Push everything back to stack1.
Here time complexity will be O(n)

deQueue(q):

If stack1 is empty then error
Pop an item from stack1 and return it
Here time complexity will be O(1)
Time Complexity:
Push operation: O(N).
In the worst case we have empty whole of stack 1 into stack 2.
Pop operation: O(1).
Same as pop operation in stack.
Auxiliary Space: O(N).
Use of stack for storing values
"""


# Python3 program to implement Queue using
# two stacks with costly enQueue()


class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self, x):

        # Move all elements from s1 to s2
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()

        # Push item into self.s1
        self.s1.append(x)

        # Push everything back to s1
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    # Dequeue an item from the queue
    def deQueue(self):

        # if first stack is empty
        if len(self.s1) == 0:
            print("Q is Empty")

        # Return top of self.s1
        x = self.s1[-1]
        self.s1.pop()
        return x


# Driver code
if __name__ == '__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)

    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())

# This code is contributed by PranchalK


"""
Method 2 is definitely better than method 1. 
Method 1 moves all the elements twice in enQueue operation, while method 2 (in deQueue operation) moves the elements 
once and moves elements only if stack2 empty. So, the amortized complexity of the dequeue operation becomes \Theta (1). 
Implementation of method 2:
"""


# Python3 program to implement Queue using
# two stacks with costly deQueue()

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    # EnQueue item to the queue
    def enQueue(self, x):
        self.s1.append(x)

    # DeQueue item from the queue
    def deQueue(self):

        # if both the stacks are empty
        if len(self.s1) == 0 and len(self.s2) == 0:
            print("Q is Empty")
            return

        # if s2 is empty and s1 has elements
        elif len(self.s2) == 0 and len(self.s1) > 0:
            while len(self.s1):
                temp = self.s1.pop()
                self.s2.append(temp)
            return self.s2.pop()

        else:
            return self.s2.pop()

# Driver code


if __name__ == '__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)

    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())

# This code is contributed by Pratyush Kumar
