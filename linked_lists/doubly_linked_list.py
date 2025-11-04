class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return str(elements)

    def is_empty(self):
        return self.head is None

    def append(self, data):
        """Add node to the end."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def prepend(self, data):
        """Add node to the start."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_at(self, index, data):
        """Insert at given index."""
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")

        if index == 0:
            self.prepend(data)
            return
        if index == self.size:
            self.append(data)
            return

        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node
        self.size += 1

    def remove(self, data):
        """Remove first occurrence of data."""
        if self.is_empty():
            raise ValueError("List is empty")

        current = self.head

        while current and current.data != data:
            current = current.next

        if not current:
            raise ValueError("Data not found in list")

        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next

        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev

        self.size -= 1

    def search(self, data):
        """Return index of first occurrence, or -1 if not found."""
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def reverse(self):
        """Reverse the list in place."""
        current = self.head
        prev = None
        self.tail = self.head

        while current:
            prev = current.prev
            current.prev = current.next
            current.next = prev
            current = current.prev

        if prev:
            self.head = prev.prev
