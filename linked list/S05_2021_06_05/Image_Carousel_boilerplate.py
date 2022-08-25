class Node:
    def __init__(self, data):

      """Implement your node variables here. This node should take next and prev values."""
        self.data = data
        self.head = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    """Implement node_push method here."""


    def list_print(node):
        while node:
            print(node.data)
            last = node
            node = node.next


    def display_image(node):
        print("Displaying image:")
        print(node.data)


    def go_forward(node):
        print("moving forward")
        display_image(node.next)
        return node.next


    def go_back(node):
        print("going back")
        display_image(node.prev)
        return node.prev

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.node_push("horse.png")
    dll.node_push("cat.png")
    dll.node_push("mouse.png")
    dll.node_push("lion.png")
    dll.node_push("hippo.png")

    list_print(dll.head)

    display_image(dll.head)
    swap = go_forward(dll.head)
    swap = go_forward(swap)
    swap = go_forward(swap)
    swap = go_back(swap)

