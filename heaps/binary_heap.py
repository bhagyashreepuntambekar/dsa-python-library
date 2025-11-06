class BinaryHeap:
    """this is implementation of min heap"""

    def __init__(self):
        self.heap = []

    def _parent(self,index):
        return (index-1)//2

    def _left(self,index):
        return (index*2) + 1

    def _right(self,index):
        return (index*2) + 2

    def insert(self,value):
        self.heap.append(value)
        self._heapify_up(len(self.heap)-1)

    def _heapify_up(self,index):
        while index > 0:
            parent = self._parent(index)
            if self.heap[index] < self.heap[parent]:
              self.heap[index],self.heap[parent]  = self.heap[parent],self.heap[index]
              index = parent
            else:
                break

    def extract_min(self):
        if not self.heap:
            raise IndexError("Heap is Empty")

        root = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._heapify_down(0)
        return root

    def _heapify_down(self,index):
        n = len(self.heap)
        while True:
            smallest = index
            left,right = self._left(index),self._right(index)

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest =  left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index],self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

    def peek(self):
        if not self.heap:
            raise IndexError("Heap is Empty")
        return self.heap[0]

    def __len__(self):
        return len(self.heap)

    def __str__(self):
        return str(self.heap)