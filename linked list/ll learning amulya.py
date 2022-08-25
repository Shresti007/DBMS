class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None  # it states linked list is empty. just now we have created linked list and no links

    # traversal through linkedList finds what happen if linked list is empty or if it is not empty. two conditions.
    # here to check second condition. we use loops, we know when to use "for loop," when we know how many times we
    # can run and we use while loop when we know stopping condition don't know wen will loop end.

    def print_LL(self):
        if self.head is None:
            print(" Linked list is empty")
        else:
            n = self.head         # a to write short term to ease the coding
            while n is not None:  # we use while loop because as we know the stopping condition.
                print(n.data, "--->", end="")
                n = n.next

    def addBegn(self, data):
        new_Node = Node(data)
        new_Node.next = self.head  # as we are inserting at beginning, we take previous first node ref from head.
        self.head = new_Node  # now head will store reference of this newly created node

    def add_end(self, data):
        new_Node = Node(data)
        if self.head is None:  # checking if linked list is empty
            self.head = new_Node  # if it is empty attach current new_node link to head.
        else:
            n = self.head  # as we are attaching link to our new node at last, for time being we are
            # turning our head func as variable "n" for self.head
            while n.next is not None:
                n = n.next
            n.next = new_Node

    def insert_afr_node(self,data,x):
        n = self.head                # Here we are referring self.head as 'n' to ease the coding.
        while n is not None:         # in order to check data of previous node, use while loop
            if x == n.data:
                break                # if we found x we will stop, so use break condition.
            n = n.next               # if x is not equal to data we searching, we wil go to next node as part increment
        if n is None:                # we are searching for "x" , if it didn't find it will print statement
            print(" node is not present in LL")
        else:
            new_Node = Node(data)
            new_Node.next = n.next
            n.next = new_Node


LL1 = LinkedList()
LL1.addBegn(10)
LL1.addBegn(50)
LL1.insert_afr_node(60,50)
LL1.add_end(1000)
LL1.print_LL()

