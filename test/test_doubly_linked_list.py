import pytest
from linked_lists.doubly_linked_list import DoublyLinkedList

def test_append_and_prepend():
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.prepend(5)
    assert str(dll) == "[5, 10, 20]"
    assert len(dll) == 3

def test_insert_at():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(3)
    dll.insert_at(1, 2)
    assert str(dll) == "[1, 2, 3]"

def test_remove():
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.remove(20)
    assert str(dll) == "[10, 30]"
    with pytest.raises(ValueError):
        dll.remove(40)

def test_search():
    dll = DoublyLinkedList()
    dll.append(5)
    dll.append(10)
    dll.append(15)
    assert dll.search(10) == 1
    assert dll.search(50) == -1

def test_reverse():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.reverse()
    assert str(dll) == "[3, 2, 1]"
