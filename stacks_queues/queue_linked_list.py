from linked_lists.singly_linked_list import SinglyLinkedList

class QueueLinkedList:
    """Queue implementation using Singly Linked List."""

    def __init__(self):
        self.list = SinglyLinkedList()
        self.tail = None  # Keep reference to tail for O(1) enqueue

    def is_empty(self):
        return len(self.list) == 0

    def enqueue(self, data):
        self.list.append(data)
        self.tail = self.list.head
        current = self.list.head
        while current and current.next:
            current = current.next
        self.tail = current

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        data = self.list.head.data
        self.list.remove(data)
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.list.head.data

    def size(self):
        return len(self.list)

    def __len__(self):
        return self.size()

    def __str__(self):
        return str(self.list)
