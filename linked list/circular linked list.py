class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularLinkedList(object):
    def __init__(self):
        self.head = None

    def traverse(self):
        #define the first node
        n = self.head
        #as long as there is a node keep going
        while n.next:         # print the data
            print(n.data)
            n = n.next        # increment the node for next traverse
            # once our n node come backs toits place after traverse end the loop
            if n == self.head:
                break

    def insert_end(self, data):    #two posibilities empty list and non empty list
        new_node = Node(data)
        # if the list is empty
        if self.head == None:
            self.head = new_node
            self.head.next = new_node # even though its only node in ll besically its just poiting to itself
            self.end = new_node       # even stating new node itself self.end too
            return
        # if the list is not empty
        if self.end != None:
            self.end.next = new_node   # in self.end node its next link is changed from self.head to new node is reffered
            new_node.next = self.head
            self.end = new_node        # so now our tail node is updated to new node
            return

    def insert_beg(self,data):         # here we can have two scenarios empty list and non empty list.
        new_node = Node(data)
        new_node.next = self.head       # our new nodes next is pointing to head so far
        curr_node = self.head           # this is the head which is been pointed as self.head before new node insertion

        # handle the emty case
        if curr_node == None:      # that mean if ll is empty
            self.head = new_node
            self.end = new_node
            self.head.next = new_node
            return

        # handle the non empty list case
        if curr_node != None:
            self.end.next = new_node       # last node is now pointing its next to our new node
            new_node.next = self.head      # so now our old head becomes next node of our new head node added at beg
            self.head = new_node           # new node becomes our self.head
            return

    def insert_mid(self, x, data):

        # handle empty node case
        if x == None:
            raise ValueError("there is Node present in ll")

        #if its the end one, use the existing insert_end method
        if x == self.end:
            self.insert_end(data)

        #if its the end one, use the existing insert_end method
        if x == self.end:
            self.insert_beg(data)

        # Otherwise it's a true mid
        new_node = Node(data)
        x_next = x.next
        x.next = new_node
        new_node.next = x_next




#define a new list
circular_list = CircularLinkedList()
# INSERT A FEW NODES
circular_list.insert_end(50)
circular_list.insert_end(50)
circular_list.insert_end(50)
# INSERT AT BEG
circular_list.insert_beg(90)
circular_list.insert_beg(100)

print('After Insertion')
print('-'*20)
circular_list.traverse()

# grab the first node