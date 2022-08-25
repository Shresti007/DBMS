class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    def __init__(self, node):
        self.root = node
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

    def make_linked_list(self, node, parent):
        """Write your code here."""

        newNode = Node(data)
        # Checks if the list is empty.
        if self.head.data is None:
            # If list is empty, both head and tail would point to new node.
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            # tail will point to new node.
            self.tail.next = newNode
            # New node will become new tail.
            self.tail = newNode
            # Since, it is circular linked list tail will point to head.
            self.tail.next = self.head


    def print_cll(self, node):
        print(node.data)
        if node.next and node.next != self.root:
            self.print_cll(node.next)


if __name__ == '__main__':
    Cll = CircularLinkedList(Node(1))
    Cll.make_linked_list(Node(2), Cll.root)
    Cll.make_linked_list(Node(3), Cll.root)
    Cll.make_linked_list(Node(4), Cll.root)
    Cll.make_linked_list(Node(5), Cll.root)
    Cll.make_linked_list(Node(6), Cll.root)
    Cll.make_linked_list(Node(7), Cll.root)
    Cll.make_linked_list(Node(8), Cll.root)


    # Printing the entire list.
    Cll.print_cll(Cll.root)