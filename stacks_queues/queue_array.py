from collections import deque

class QueueArray:
    """Queue implementation using deque for O(1) operations."""

    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        """Add element to the back."""
        self.items.append(item)

    def dequeue(self):
        """Remove element from the front."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.popleft()

    def peek(self):
        """Return the front element without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[0]

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()

    def __str__(self):
        return str(list(self.items))
