class Stack:
    def __init__(self, content=None):
        self._stack = list(content) if content else []

    def is_empty(self):
        return len(self._stack) == 0

    def push(self, el):
        self._stack.append(el)

    def pop(self):
        if self.is_empty():
            raise IndexError("Couldn't pop from empty stack")
        return self._stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Couldn't peek from empty stack")
        return self._stack[-1]

    def size(self):
        return len(self._stack)
