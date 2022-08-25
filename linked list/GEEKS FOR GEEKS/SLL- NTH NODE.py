# A complete working Python program to find n'th node
# in a linked list

# Node class


class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # This function is in LinkedList class. It inserts
    # a new node at the beginning of Linked List.

    def push(self, new_data):

        # 1 & 2: Allocate the Node &
        #	 Put in the data
        new_node = Node(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node

    # Returns data at given index in linked list
    def getNth(self, index):
        current = self.head  # Initialise temp
        count = 0  # Index of current node

        # Loop while end of linked list is not reached
        while (current):
            if (count == index):
                return current.data
            count += 1
            current = current.next

        # if we get to this line, the caller was asking
        # for a non-existent element so we assert fail
        assert (false)
        return 0


# Driver Code
if __name__ == '__main__':
    llist = LinkedList()

    # Use push() to construct below list
    # 1->12->1->4->1
    llist.push(1)
    llist.push(4)
    llist.push(1)
    llist.push(12)
    llist.push(1)

    n = 3
    print("Element at index 3 is :", llist.getNth(n))

""""
N TH NODE FROM END OF SLL
"""


# Simple Python3 program to find
# n'th node from end
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # createNode and and make linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Function to get the nth node from
    # the last of a linked list
    def printNthFromLast(self, n):
        temp = self.head  # used temp variable

        length = 0
        while temp is not None:
            temp = temp.next
            length += 1

        # print count
        if n > length:  # if entered location is greater
            # than length of linked list
            print('Location is greater than the' +
                  ' length of LinkedList')
            return
        temp = self.head
        for i in range(0, length - n):
            temp = temp.next
        print(temp.data)


# Driver Code
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(35)


# This code is contributed by Yogesh Joshi
"""
ANOTHER APPROACH TO FIND N TH ELEMENT
"""


# Python program to find n'th node from end using slow
# and fast pointer

# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printNthFromLast(self, n):
        main_ptr = self.head
        ref_ptr = self.head

        count = 0
        if self.head is not None:
            while count < n:
                if ref_ptr is None:
                    print("% d is greater than the no.pf nodes in list" %(n)
                return

            ref_ptr = ref_ptr.next
            count += 1

        if (ref_ptr is None):
            self.head = self.head.next
            if (self.head is not None):
                print
                "Node no. % d from last is % d "
                % (n, main_ptr.data)

        else:


            while (ref_ptr is not None):
                main_ptr = main_ptr.next
                ref_ptr = ref_ptr.next

            print( "Node no. % d from last is % d ", %(n, main_ptr.data))

# Driver program to test above function
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(35)

llist.printNthFromLast(4)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

