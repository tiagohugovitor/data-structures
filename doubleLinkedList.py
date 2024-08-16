class ListNode:
    def __init__(self, val, previous=None, next=None):
        self._previous = previous
        self._val = val
        self._next = next

class DoubleLinkedList:
    def __init__(self):
        self._head = None 
        self._tail = None

    def search(self, val):
        current = self._head
        while current and current._val != val:
            current = current._next 
        return current

    def insert_start(self, val):
        current = self._head
        el = ListNode(val)
        self._head = el
        if current is None:
            self._tail = el
            return
        current._previous = el
        el._next = current

    def insert_end(self, val):
        current = self._tail
        el = ListNode(val)
        self._tail = el
        if current is None:
            self._head = el
            return
        current._next = el
        el._previous = current

    def delete(self, val):
        el = self.search(val)
        if el is None:
            raise IndexError('Element not found to be deleted')
        if el._previous == None:
            self._head = el._next
        else:
            el._previous._next = el._next
        if el._next == None:
            self._tail = el._previous
        else:
            el._next._previous = el._previous
        return el
    
    def print_list(self):
        current = self._head
        while current:
            print(f'{current._val} -> ', end='')
            current = current._next
        print('None')

    def create_list_from_array(self, array):
        if not array:
            return
        self._head = ListNode(array[0])
        current = self._head
        for val in array[1:]:
            el = ListNode(val)
            current._next = el
            el._previous = current
            current = current._next
        self._tail = current
