class Queue:

    def __init__(self, maxsize):
        self.queue = []           # empty list
        self.front = -1           # initially representing queue as empty
        self.rear = -1            # initially representing queue as empty
        self.maxsize = maxsize    # just passing size parameter

    def enqueue(self, item):
        if self.rear == self.maxsize - 1:   # check whether queue is full
            print("Overflow")
            return
        if self.rear == -1:  # if queue is not completely full, check whether it is  first element being added.
            self.rear += 1   # if so first element updated we update both rear and front
        else:                # if it is not first element being updated
            self.rear += 1

        self.queue.append(item)  # so now we can simply append in queue if any above is matched rather than first
        print(item, "inserted.")

    def display(self):
        for i in range(self.front, self.rear+1):  # from front to till end rear last
            print(self.queue[i])

    def isEmpty(self):
        if self.front == -1:
            return True
        return False

    def dequeue(self):   # deleting/removing an item from queue
        if self.isEmpty():     # you can use self.front == -1
            return "Queue is Under flow"
        tmp = self.front       # just hold the element which is going to be deleted for a while
        if self.front == self.rear: # check whether we are holing only one element or not, if so this condition will act
            self.front = self.rear = -1 # so after deleting one element present, now queue will be empty
        self.front = self.front + 1  # we are now incrementing front field as ele is deleted.

        return self.queue[tmp]   # now return the element present in queue to


queue = Queue(3)
print("count of element: ", queue.isEmpty())
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
print("Removed element:", queue.dequeue())
queue.display()
