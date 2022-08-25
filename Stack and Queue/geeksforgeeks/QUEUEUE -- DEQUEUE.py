"""
Deque or Double Ended Queue is a generalized version of Queue data structure that allows insert and delete at both ends.

Operations on Deque:
Mainly the following four basic operations are performed on queue:

insertFront(): Adds an item at the front of Deque.
insertLast(): Adds an item at the rear of Deque.
deleteFront(): Deletes an item from front of Deque.
deleteLast(): Deletes an item from rear of Deque.

In addition to above operations, following operations are also supported
getFront(): Gets the front item from queue.
getRear(): Gets the last item from queue.
isEmpty(): Checks whether Deque is empty or not.
isFull(): Checks whether Deque is full or not.

Applications of Deque:
Since Deque supports both stack and queue operations, it can be used as both. The Deque data structure supports clockwi
se and anticlockwise rotations in O(1) time which can be useful in certain applications.
Also, the problems where elements need to be removed and or added both ends can be efficiently solved using Deque. For
example see Maximum of all subarrays of size k problem., 0-1 BFS and Find the first circular tour that visits all petr
"""
# Deque (Doubly Ended Queue) in Python is implemented using the module “collections“. Deque is preferred over list in
# the cases where we need quicker append and pop operations from both the ends of container, as deque provides an O(
# 1) time complexity for append and pop operations as compared to list which provides O(n) time complexity. Python
# code to demonstrate deque
from collections import deque

# Declaring deque
queue = deque(['name', 'age', 'DOB'])
print(queue)
"""
append() :- This function is used to insert the value in its argument to the right end of deque.
appendleft() :- This function is used to insert the value in its argument to the left end of deque.
pop() :- This function is used to delete an argument from the right end of deque.
popleft() :- This function is used to delete an argument from the left end of deque.
"""
# Python code to demonstrate working of
# append(), appendleft(), pop(), and popleft()

# importing "collections" for deque operations
import collections

# initializing deque
de = collections.deque([1,2,3])
# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)
# printing modified deque
print ("The deque after appending at right is : ")
print (de)
# using appendleft() to insert element at left end
# inserts 6 at the beginning of deque
de.appendleft(6)
# printing modified deque
print ("The deque after appending at left is : ")
print (de)
# using pop() to delete element from right end
# deletes 4 from the right end of deque
de.pop()
# printing modified deque
print ("The deque after deleting from right is : ")
print (de)
# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()
# printing modified deque
print ("The deque after deleting from left is : ")
print (de)

""""
index(ele, beg, end) :- This function returns the first index of the value mentioned in arguments, starting searching 
from beg till end index.
insert(i, a) :- This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.
remove() :- This function removes the first occurrence of value mentioned in arguments. 
count() :- This function counts the number of occurrences of value mentioned in arguments. 
"""

# Python code to demonstrate working of
# insert(), index(), remove(), count()

# importing "collections" for deque operations

# initializing deque
de = collections.deque([1, 2, 3, 3, 4, 2, 4])

# using index() to print the first occurrence of 4
print ("The number 4 first occurs at a position : ")
print (de.index(4,2,5))

# using insert() to insert the value 3 at 5th position
de.insert(4,3)

# printing modified deque
print ("The deque after inserting 3 at 5th position is : ")
print (de)

# using count() to count the occurrences of 3
print ("The count of 3 in deque is : ")
print (de.count(3))

# using remove() to remove the first occurrence of 3
de.remove(3)

# printing modified deque
print ("The deque after deleting first occurrence of 3 is : ")
print (de)


"""
extend(iterable) :- This function is used to add multiple values at the right end of deque. The argument passed is an it
erable.
 
extendleft(iterable) :- This function is used to add multiple values at the left end of deque. The argument passed is an
 iterable. Order is reversed as a result of left appends.
 
reverse() :- This function is used to reverse order of deque elements.
 
rotate() :- This function rotates the deque by the number specified in arguments. If the number specified is negative,
 rotation occurs to left. Else rotation is to right.
"""

# Python code to demonstrate working of
# extend(), extendleft(), rotate(), reverse()

# importing "collections" for deque operations
import collections

# initializing deque
de = collections.deque([1, 2, 3,])

# using extend() to add numbers to right end
# adds 4,5,6 to right end
de.extend([4,5,6])

# printing modified deque
print ("The deque after extending deque at end is : ")
print (de)

# using extendleft() to add numbers to left end
# adds 7,8,9 to right end
de.extendleft([7,8,9])

# printing modified deque
print ("The deque after extending deque at beginning is : ")
print (de)

# using rotate() to rotate the deque
# rotates by 3 to left
de.rotate(-3)

# printing modified deque
print ("The deque after rotating deque is : ")
print (de)

# using reverse() to reverse the deque
de.reverse()

# printing modified deque
print ("The deque after reversing deque is : ")
print (de)
