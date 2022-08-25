#from exceptions import Empty
class ArrayQueue:

    def __init__(self):
        self._data = []
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size ==0

    def enqueue(self, data):
        self._data.append(data)
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty("queue is empty")
        value = self._data[self._front] = None
        self._front = self._front + 1
        self._size = self._size -1
        return value

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    @property
    def data(self):
        return self._data


q = ArrayQueue()
q.enqueue(10)
q.enqueue(20)
print('Queue: ', q.data)
print("Length: ",len(q))
print("Dequeue: ", q.dequeue())
print("Queue: ", q.data)
q.enqueue(30)
q.enqueue(40)
print("Queue: ", q.data)
print("First Element: ", q.first())
print("Queue: ", q.data)
print("Dequeue: ", q.dequeue())
print(("Queue: ", q.data))


