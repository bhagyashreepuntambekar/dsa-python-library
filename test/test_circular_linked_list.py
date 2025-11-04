import pytest
from linked_lists.circular_linked_list import CircularLinkedList

def test_append_and_str():
    cll = CircularLinkedList()
    cll.append(10)
    cll.append(20)
    cll.append(30)
    assert str(cll) == "[10, 20, 30]"
    assert len(cll) == 3

def test_prepend():
    cll = CircularLinkedList()
    cll.append(10)
    cll.prepend(5)
    assert str(cll) == "[5, 10]"

def test_insert_at():
    cll = CircularLinkedList()
    cll.append(1)
    cll.append(3)
    cll.insert_at(1, 2)
    assert str(cll) == "[1, 2, 3]"

def test_remove():
    cll = CircularLinkedList()
    cll.append(1)
    cll.append(2)
    cll.append(3)
    cll.remove(2)
    assert str(cll) == "[1, 3]"
    with pytest.raises(ValueError):
        cll.remove(5)

def test_search():
    cll = CircularLinkedList()
    cll.append(10)
    cll.append(20)
    cll.append(30)
    assert cll.search(20) == 1
    assert cll.search(40) == -1
