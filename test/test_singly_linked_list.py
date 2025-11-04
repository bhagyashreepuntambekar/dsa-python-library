import pytest
from linked_lists.singly_linked_list import SinglyLinkedList

def test_append():
    ll = SinglyLinkedList()
    ll.append(10)
    ll.append(20)
    assert len(ll) == 2
    assert str(ll) == "[10, 20]"

def test_prepend():
    ll = SinglyLinkedList()
    ll.append(10)
    ll.prepend(5)
    assert str(ll) == "[5, 10]"

def test_insert_at():
    ll = SinglyLinkedList()
    ll.append(1)
    ll.append(3)
    ll.insert_at(1, 2)
    assert str(ll) == "[1, 2, 3]"

def test_remove():
    ll = SinglyLinkedList()
    ll.append(10)
    ll.append(20)
    ll.remove(10)
    assert str(ll) == "[20]"
    with pytest.raises(ValueError):
        ll.remove(30)

def test_search():
    ll = SinglyLinkedList()
    ll.append(5)
    ll.append(10)
    ll.append(15)
    assert ll.search(10) == 1
    assert ll.search(50) == -1
