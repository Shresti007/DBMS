"""
Question: Design a Data Structure SpecialStack that supports all the stack operations like push(), pop(),
isEmpty(), isFull() and an additional operation getMin() which should return minimum element from the SpecialStack.
All these operations of SpecialStack must be O(1). To implement SpecialStack, you should only use standard Stack data
structure and no other data structure like arrays, list, . etc.
"""

"""
Consider the following SpecialStack
16  --> TOP
15
29
19
18

When getMin() is called it should 
return 15, which is the minimum 
element in the current stack. 

If we do pop two times on stack, 
the stack becomes
29  --> TOP
19
18

When getMin() is called, it should 
return 18 which is the minimum in 
the current stack.
Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.
Solution: Use two stacks: one to store actual stack elements and the other as an auxiliary stack to store minimum values
. The idea is to do push() and pop() operations in such a way that the top of the auxiliary stack is always the minimum.
 Let us see how push() and pop() operations work.

Push(int x) // inserts an element x to Special Stack 
1) push x to the first stack (the stack with actual elements) 
2) compare x with the top element of the second stack (the auxiliary stack). Let the top element be y. 
…..a) If x is smaller than y then push x to the auxiliary stack. 
…..b) If x is greater than y then push y to the auxiliary stack.
int Pop() // removes an element from Special Stack and return the removed element 
1) pop the top element from the auxiliary stack. 
2) pop the top element from the actual stack and return it.
Step 1 is necessary to make sure that the auxiliary stack is also updated for future operations.
int getMin() // returns the minimum element from Special Stack 
1) Return the top element of the auxiliary stack.

We can see that all the above operations are O(1). 
Let us see an example. Let us assume that both stacks are initially empty and 18, 19, 29, 15, and 16 are inserted to 
the SpecialStack. 
When we insert 18, both stacks change to following.
Actual Stack
18 <--- top     
Auxiliary Stack
18 <---- top

When 19 is inserted, both stacks change to following.
Actual Stack
19 <--- top     
18
Auxiliary Stack
18 <---- top
18

When 29 is inserted, both stacks change to following.
Actual Stack
29 <--- top     
19
18
Auxiliary Stack
18 <---- top
18
18

When 15 is inserted, both stacks change to following.
Actual Stack
15 <--- top     
29
19 
18
Auxiliary Stack
15 <---- top
18
18
18

When 16 is inserted, both stacks change to following.
Actual Stack
16 <--- top     
15
29
19 
18
Auxiliary Stack
15 <---- top
15
18
18
18
The following is the implementation for SpecialStack class. In the below implementation, SpecialStack inherits from 
Stack and has one Stack object min which works as an auxiliary stack.
"""


# Python3 program for the
# above approach
# A simple stack class with
# basic stack funtionalities
class stack:


    def __init__(self):
        self.array = []
        self.top = -1
        self.max = 100


    # Stack's member method to check
    # if the stack is empty
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False


    # Stack's member method to check
    # if the stack is full
    def isFull(self):
        if self.top == self.max - 1:
            return True
        else:
            return False


    # Stack's member method to
    # insert an element to it

    def push(self, data):
        if self.isFull():
            print('Stack OverFlow')
        return
        else:
        self.top += 1
        self.array.append(data)


    # Stack's member method to
    # remove an element from it
    def pop(self):
        if self.isEmpty():
            print('Stack UnderFlow')
        return
        else:
        self.top -= 1
        return self.array.pop()


# A class that supports all the stack
# operations and one additional
# operation getMin() that returns the
# minimum element from stack at
# any time. This class inherits from
# the stack class and uses an
# auxiliary stack that holds
# minimum elements
class SpecialStack(stack):


    def __init__(self):
        super().__init__()
        self.Min = stack()


    # SpecialStack's member method to
    # insert an element to it. This method
    # makes sure that the min stack is also
    # updated with appropriate minimum
    # values
    def push(self, x):
        if self.isEmpty():
            super().push(x)
        self.Min.push(x)
        else:
        super().push(x)
        y = self.Min.pop()
        self.Min.push(y)
        if x <= y:
            self.Min.push(x)
        else:
            self.Min.push(y)


    # SpecialStack's member method to
    # remove an element from it. This
    # method removes top element from
    # min stack also.
    def pop(self):
        x = super().pop()
        self.Min.pop()
        return x


    # SpecialStack's member method
    # to get minimum element from it.
    def getmin(self):
        x = self.Min.pop()
        self.Min.push(x)
        return x


# Driver code
if __name__ == '__main__':

s = SpecialStack()
s.push(10)
s.push(20)
s.push(30)
print(s.getmin())
s.push(5)
print(s.getmin())

# This code is contributed by rachitkatiyar99


