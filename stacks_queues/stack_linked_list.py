from linked_lists.singly_linked_list import SinglyLinkedList

class StackLinkedList:
    """Stack implementation using a Singly Linked List."""

    def __init__(self):
        self.list = SinglyLinkedList()

    def is_empty(self):
        return len(self.list) == 0

    def push(self, data):
        self.list.prepend(data)  # push to head for O(1)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        data = self.list.head.data
        self.list.remove(data)
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.list.head.data

    def size(self):
        return len(self.list)

    def __len__(self):
        return self.size()

    def __str__(self):
        # Top of stack = head
        return f"Top -> {self.list}"
