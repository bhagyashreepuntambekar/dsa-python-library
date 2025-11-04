class DynamicArray:
    def __init__(self):
        self._capacity = 1
        self._size = 0
        self._data = [None] * self._capacity

    def __len__(self):
        return self._size

    def __str__(self):
        return str([self._data[i] for i in range(self._size)])

    def _resize(self, new_cap):
        new_data = [None] * new_cap
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_cap

    def append(self, value):
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = value
        self._size += 1

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        return self._data[index]

    def set(self, index, value):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        self._data[index] = value

    def remove_last(self):
        if self._size == 0:
            raise IndexError("Array is empty")
        value = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        if 0 < self._size <= self._capacity // 4:
            self._resize(max(1, self._capacity // 2))
        return value
