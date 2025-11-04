class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.head is None

    def __str__(self):
        elements = []
        if self.is_empty():
            return str(elements)

        current = self.head
        while True:
            elements.append(current.data)
            current = current.next
            if current == self.head:
                break
        return str(elements)

    def append(self, data):
        """Add node to the end."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1


    def prepend(self, data):
        """Add node at the start."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.size += 1

    def insert_at(self, index, data):
        """Insert at a given index."""
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
        current.next = new_node
        self.size += 1

    def remove(self, data):
        """Remove first occurrence of data."""
        if self.is_empty():
            raise ValueError("List is empty")

        current = self.head
        prev = self.tail
        while True:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                    self.tail.next = self.head
                elif current == self.tail:
                    self.tail = prev
                    self.tail.next = self.head
                else:
                    prev.next = current.next
                self.size -= 1
                if self.size == 0:
                    self.head = None
                    self.tail = None
                return
            prev = current
            current = current.next
            if current == self.head:
                break
        raise ValueError("Data not found in list")

    def search(self, data):
        """Return index of first occurrence, or -1 if not found."""
        if self.is_empty():
            return -1

        current = self.head
        index = 0
        while True:
            if current.data == data:
                return index
            current = current.next
            index += 1
            if current == self.head:
                break
        return -1