class Queue:
    # We use a basic list to implement a Queue data structure
    def __init__(self):
        self._queue = []

    # Return true if queue is empty
    def empty(self):
        # Implement the logic and remove 'pass'
        if self._queue is None:          # check the queue emptiness
            return True                  # if so return true
        return False                     # else state queue is empty


    # Returns the length of the queue
    def size(self):
        # Implement the logic and remove 'pass'
        return len(self._queue)                   # states capacity of queue

    # Enqueues an item to the end of the queue
    def enqueue(self,item):
        # Implement the logic and remove 'pass'
        self._queue.append(item)                  # add the songs in the queue

    # Dequeues an item from the front of the queue
    # It returns None if the queue is empty
    def dequeue(self):
        # Implement the logic and remove 'pass'
        if len(self._queue) > 0:                  # if queue is not empty
            return self._queue.pop(0)             # remove the song from the queue
        else:
            return None                           # it states no more songs left in queue

    # Returns the item at the front of the queue without removing it
    # Sometimes you need to peek at the value but not remove it from the queue yet
    # It returns None if the queue is empty
    def front(self):
        if not self.empty():                      # conditioning queue is not empty then
            return self._queue[0]                 # as FIFO basis we pull first song in index 0
        else:
            return None                           # nothing is left to pull

    # Returns the item at the rear of the queue without removing it
    # Sometimes you need to peek at the value but not remove it from the queue yet
    # It returns None if the queue is empty
    def rear(self):
        # Implement the logic and remove 'pass'
        if not self.empty():                      # checking is queue empty or what?
            return self._queue[-1]                # returns last item present in queue
        return None





