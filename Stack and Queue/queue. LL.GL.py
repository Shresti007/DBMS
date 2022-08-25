class QNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.front = None       # new class has been created , yet no nodes are present to link or place them.
        self.rear = None        # new class has been created , yet no nodes are present to link or place them.

    def enqueue(self, item):
        new_node = QNode(item)  # as it is enqueue operation we are going to add new_node's with their data.
        if self.rear is None:   # assuming if no nodes is present and class is empty
            self.front = self.rear = new_node # so in this case only one node present, front and rear point's same node
        self.rear.next = new_node  # else if nodes present in class, then our new_node will be next to current rear
        self.rear = new_node      # now new_node will be acting as self.rear as it is end of queue

    def display(self):
        new_node = self.front    # a temporay node created to hold front
        while new_node:          # while temp node is not none
            print(new_node.data)
            new_node = new_node.next  # incrementing

    def isEmpty(self):   # if we check for front ele we can understand
        if self.front is None:
            return True
        return False

    def dequeue(self):
        if self.isEmpty():
            return "Underflow: Queue is empty! "
        tmp = self.front             # hold the node deleting with this tmp queue
        self.front = tmp.next        # updating tmp with its next
        if self.front is None:
            self.rear = None
        return tmp.data              # now return the element present in queue


queue = Queue()
print("Empty: ", queue.isEmpty())
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
print("Dequeued element: ", queue.dequeue())
print(queue.display())


