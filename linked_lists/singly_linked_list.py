class Node:
    def __init__(self,data):
        self.data =  data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
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

    def append(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size +=1

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size +=1

    def insert_at(self,index,data):
        if index<0 or index>self.size:
            raise IndexError("Index out of range")

        if index == 0:
            self.prepend(data)
            return

        new_node = Node(data)
        current = self.head

        for _ in range(index-1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size +=1

    def remove(self,data):
        if self.is_empty():
            raise ValueError("List is empty")

        if self.head.data == data:
            self.head = self.head.next
            self.size -=1
            return

        current = self.head
        prev = None

        while current and current.data!=data:
            prev = current
            current = current.next

        if current is None:
            raise ValueError("Data not found in the list")

        prev.next = current.next

        self.size -=1

    def search(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1
