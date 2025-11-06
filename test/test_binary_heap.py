from heaps.binary_heap import BinaryHeap
import pytest

def test_insert_and_peek():
    heap = BinaryHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(8)
    heap.insert(1)

    assert heap.peek() == 1
    assert len(heap) == 4

def test_extract_min():
    heap = BinaryHeap()
    for x in [5, 3, 8, 1, 2]:
        heap.insert(x)

    result = [heap.extract_min() for _ in range(len(heap))]
    assert result == [1, 2, 3, 5, 8]

def test_extract_from_empty():
    heap = BinaryHeap()
    with pytest.raises(IndexError):
        heap.extract_min()
