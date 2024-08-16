class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class List:
    def __init__(self):
        self._head = None
        self._tail = None

    def search(self, val):
        current = self._head
        
        while current and current.val != val:
            current = current.next
        
        return current

    def insert_start(self, val):
        newHead = ListNode(val, self._head)
        self._head = newHead
        if self._tail is None:
            self._tail = newHead

    def insert_end(self, val):
        newTail = ListNode(val)
        if self._head is None:
            self._head = newTail
            self._tail = newTail
            return
        self._tail.next = newTail
        self._tail = newTail

    def delete(self, val):
        current = self._head
        previous = None
        
        while current and current.val != val:
            previous = current
            current = current.next

        if current is None:
            raise IndexError('Node not found to delete')
        
        if previous is None:
            self._head = current.next
        else:
            previous.next = current.next

        if self._tail == current:
            self._tail = previous

        if self._head is None:
            self._tail = None

        return current
    
    def print_list(self):
        current = self._head
        while current:
            print(f'{current.val} -> ', end='')
            current = current.next
        print('None')
        
    def create_list_from_array(self, array):
        if not array:
            self._head = None
            self._tail = None
            return
        
        self._head = ListNode(array[0])
        current = self._head
        for val in array[1:]:
            current.next = ListNode(val)
            current = current.next
        self._tail = current 
