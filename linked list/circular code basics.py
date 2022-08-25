class Node(object):
    def __init__(self, data= None, next = None):
        self.data = data
        self.next = next
        self.prev = None


class CircularLinkedList(object):
    def __init__(self, head = None, end = None):
        self.head = None
        self.end = end

    def traverse(self):
        #define ifrst node
        n = self.head
        # as long as there next node keep going
        while n.next:
            print(n.data)
            n = n.next

            # once we get back to head end the loop
            if n == self.head:
                break

    def insert_end(self, data):
        new_node = Node(data) # during empty case

        # if the list is empty
        if self.head is None:
            self.head = new_node
            self.head.next = new_node
            self.end = new_node
            return
        # if list is not empty
        if self.end is not None:
            self.end.next = new_node
            new_node.next = self.head
            self.end = new_node
            return

    def insert_beg(self,data):
        new_node = Node(data)
        new_node.next = self.head
        new_node = self.head

        # handle while cll is empty
        if self.head is None:
            self.head = new_node
            self.end = new_node
            self.head.next = new_node
            return

        # handle the non empty list case
        if self.end is not None:
            self.end.next = new_node
            new_node.next = self.head
            self.head = new_node
            return


CLL = CircularLinkedList()

CLL.insert_end(50)
CLL.insert_end(60)
CLL.insert_end(70)
CLL.insert_end(80)

CLL.insert_beg(20)
CLL.insert_beg(30)

print(" After Insertion")
print('-'*20)
CLL.traverse()



