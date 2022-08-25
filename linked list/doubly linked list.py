class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLLinkedList:
    def __init__(self):
        self.head = None  # initially considering Dll as empty while creating ll class

    # Forward Traversing:
    def print_LL(self):
        if self.head is None:  # here it is referring to first node
            print("Linked List is empty!")
        else:
            n = self.head  # for better minimal letter for better coding
            while n is not None:
                print(n.data, "--->", end = " ")
                n = n.next  # incrementing for next ref

    # Backward Traversing:
    def print_LL_reverse(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n.next is not None:  # because we want to traverse from last so as last node is having null we use
                # while loop as we know stopping condition. still it finds last node it traverse.
                n = n.next
            while n is not None:
                print(n.data, "--->", end = " ")
                n = n.prev

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node         # it mean pointing head to new node
        else:
            print("Linked List is not empty!")

    def add_begin(self, data, prev = None):
        new_node = Node(data)            # passing parameter as new node created for this function
        if self.head is None:            # if ll is empty
            self.head = new_node         # here head is pointing to new node and new node link is stored in head
        else:                            # if ll is non empty
            new_node.next = self.head    # new inseerted one wants to be stat node, so it will takes link of actual
            # first node link from head and stat acts as firstnode
            self.head.prev = new_Node    # here head node prev is stored with link of our new head
            self.head = new_node         # now head points it line to new node, node becomes head of nodes

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next                # this is way we go till last node
            n.next = new_node             # so after going to last node our new node is attached to it
            new_node.prev = n              # now actual last one become n nothing but self.head

    def add_after(self, data, x):
        if self.head is None:  # check whether ll is empty
             print("LL is empty!")
        else:
            n = self.head  # for better optimization of code we are taking short variable for self.head
            while n is not None:  # as n is not none. it mean ll is not empty, so check for x variable
                if x == n.data:  # if this x is equal then break statement brings it from inside loop
                    break
                n = n.next  # if x is not value we are checking in node, it will go to another node using link in node
            if n is None:  #
                print("Given Node is not present in DLL")
            else:
                new_node = Node(data)
                new_node.next = n.next  # here we are attaching link of next ref to our created node. as in previous
                # node it is n.next we brink link and attached to new node
                new_node.prev = n  # new node prev is attached and we linked the xvalue node in between two node
                if n.next is not None:  # checking if we are inserting after last node
                    n.next.prev = new_node  # here right node prev is getting allocated our new_node link on it
                n.next = new_node  # here in x node it's next link is attached to new node

    def add_before(self, data, x):
        if self.head is None:
            print("LL is empty!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.next
            if n is None:
                print("Given Node is not present in DLL")
            else:
                new_node = Node(data)  # check whether u r creating new_node before x
                new_node.next = n  # here foe new node link of x is attached
                new_node.prev = n.prev  # for new node prev, of x node is attached, inx node t is called as n. prev
                if n.prev is not None:  # checking to be clear new_node is not starting node.
                    n.prev.next = new_node  # as it is in n node its prev is as prev and node name n
                    # so  it is n.prev in its field
                else:
                    self.head = new_node  # we just attaching it before first node
                n.prev = new_node

    def delete_begin(self):
        if self.head is None:  # here ll is empty no node at all
            print("DLL is empty can't delte !")
            return
        if self.head.next is None:  # heer thre exist only one node
            self.head = None
            print("DLL is empty after deleting the node!")
        else:
            self.head = self.head.next  # here next node becomes head node
            self.head.prev = None  # as next node become head node, its link in prev field is deleted

    def delete_end(self):
        if self.head is None:  # here no nodel at all in ll
            print("DLL is empty can't delte !")
            return
        if self.head.next is None:  # here when ll consist of only one node
            self.head = None
            print("DLL is empty after deleting the node!")
        else:
            n = self.head              # here we are trying to find last node with null next link defining it as n
            while n.next is not None:  # while traversing if we didnt find node with nul at end
                n = n.next             # we wll go to next node and stop where node's next is null, it becomes n now.
            n.prev.next = None  # so in n node it is shown as n.prev .. so as we deleting n node its previous node
            # become n.prev.next = 0

    def delete_by_value(self, x):
        if self.head is None:  # if there is no node in ll
            print("DLL is empty can't delte !")
            return
        if self.head.next is None:  # if there is only one node present in ll
            if x == self.head.data:
                self.head = None    # if x value is present in only node after deleting it becomes dll empty
            else:
                print("x is not present in DLL")
            return
        if self.head.data == x:  # here if we are deleting first node
            self.head = self.head.next  # here next node becomes self.head so deleting node writes
            self.head.prev = None  # new self.head preview will be as null, as its point is get delet
            return
        n = self.head  # here we are searching for node in middle nodes by value x
        while n.next is not None:  # here it search for x value. condition states its not checking
            # for last node, where normally last node has null value
            if x == n.data:
                break  # if it founds value, it comes out from loop using break
            n = n.next
        if n.next is not None:  # here if break statement is executed.
            n.next.prev = n.prev  # here in n books we have written our next node as n.next, so as
            # we are deleting n .we have to connect it by n.next.prev = n.prev for next node books
            n.prev.next = n.next  # as n node is getting deleted in previous nodes next link ref is
            # as if we see from n it is n.previous and inorder to connect to next node of n it is next so after deleting
            # they are connected by in terms of previous node as n.prev.next = n.next in previous node books
        else:
            if n.data == x:  # if last node is x
                n.prev.next = None  # so in n books its previous link and pre boooks its next link is
                # been deleted by passing arg as n.prev.next = None
            else:
                print("x is not present in dll!")


new_node = DLLinkedList()
new_node.add_begin(4)
new_node.add_before(50,10)
new_node.add_after(4,10)
new_node.print_LL()
