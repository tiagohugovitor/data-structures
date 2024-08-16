class MyQueue:
    def __init__(self, content=None):
        self._queue = list(content) if content else []

    def is_empty(self):
        return len(self._queue) == 0

    def enqueue(self, el):
        self._queue.append(el)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Couldn't dequeue from empty queue")
        val = self._queue[0]
        self._queue.remove(val)
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError("Couldn't peek from empty queue")
        return self._queue[0]

    def size(self):
        return len(self._queue)


from collections import deque

class Queue:
    def __init__(self, content=None):
        self._queue = deque(content) if content else deque()

    def is_empty(self):
        return len(self._queue) == 0

    def enqueue(self, el):
        self._queue.append(el)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Couldn't dequeue from empty queue")
        return self._queue.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("Couldn't peek from empty queue")
        return self._queue[0]

    def size(self):
        return len(self._queue)
