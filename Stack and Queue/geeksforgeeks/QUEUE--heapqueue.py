import heapq
"""Heap data structure is mainly used to represent a priority queue. In Python, it is available using “heapq” module.
The property of this data structure in Python is that each time the smallest of heap element is popped(min heap).
Whenever elements are pushed or popped, heap structure in maintained. The heap[0] element also returns the smallest
element each time.

Let’s see various Operations on heap :

heapify(iterable) :- This function is used to convert the iterable into a heap data structure. i.e. in heap order.

heappush(heap, ele) :- This function is used to insert the element mentioned in its arguments into heap. The order is
adjusted, so as heap structure is maintained.
heappop(heap) :- This function is used to remove and return the smallest element from heap. The order is adjusted, so
as heap structure is maintained.
"""
# Python code to demonstrate working of
# heapify(), heappush() and heappop()

# importing "heapq" to implement heap queue
# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print ("The created heap is : ",end="")
print (list(li))

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li,4)

# printing modified heap
print ("The modified heap after push is : ",end="")
print (list(li))

# using heappop() to pop smallest element
print ("The popped and smallest element is : ",end="")
print (heapq.heappop(li))


# Python code to demonstrate working of
# heappushpop() and heapreplce()

# importing "heapq" to implement heap queue


# initializing list 1
li1 = [5, 7, 9, 4, 3]

# initializing list 2
li2 = [5, 7, 9, 4, 3]

# using heapify() to convert list into heap
heapq.heapify(li1)
heapq.heapify(li2)

# using heappushpop() to push and pop items simultaneously
# pops 2
print ("The popped item using heappushpop() is : ",end="")
print (heapq.heappushpop(li1, 2))

# using heapreplace() to push and pop items simultaneously
# pops 3
print ("The popped item using heapreplace() is : ",end="")
print (heapq.heapreplace(li2, 2))


# nlargest(k, iterable, key = fun) :- This function is used to return the k largest elements from the iterable
# specified and satisfying the key if mentioned.

# nsmallest(k, iterable, key = fun) :- This function is used to return the k smallest elements from the iterable
# specified and satisfying the key if mentioned.

# Python code to demonstrate working of
# nlargest() and nsmallest()

# importing "heapq" to implement heap queue

# initializing list
li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]

# using heapify() to convert list into heap
heapq.heapify(li1)

# using nlargest to print 3 largest numbers
# prints 10, 9 and 8
print("The 3 largest numbers in list are : ",end="")
print(heapq.nlargest(3, li1))

# using nsmallest to print 3 smallest numbers
# prints 1, 3 and 4
print("The 3 smallest numbers in list are : ",end="")
print(heapq.nsmallest(3, li1))



