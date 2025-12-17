from heaps.binary_heap import BinaryHeap


class PriorityQueues:
    def __init__(self):
        self.heap = BinaryHeap()

    def push(self,priority,value):
        self.heap.insert((priority,value))

    def pop(self):
        if len(self.heap) == 0:
            raise IndexError("Priority Queue is empty")
        return self.heap.extract_min()

    def peek(self):
        return self.heap.peek()

    def is_empty(self):
        return len(self.heap) == 0

    def __len__(self):
        return len(self.heap)