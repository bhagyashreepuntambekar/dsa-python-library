import pytest
from arrays.dynamic_array import DynamicArray

def test_append_and_get():
    arr = DynamicArray()
    arr.append(10)
    arr.append(20)
    assert len(arr) == 2
    assert arr.get(0) == 10
    assert arr.get(1) == 20

def test_set():
    arr = DynamicArray()
    arr.append(5)
    arr.set(0, 15)
    assert arr.get(0) == 15

def test_remove_last():
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    value = arr.remove_last()
    assert value == 2
    assert len(arr) == 1

def test_index_out_of_bounds():
    arr = DynamicArray()
    arr.append(5)
    with pytest.raises(IndexError):
        arr.get(5)
