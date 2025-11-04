import pytest
from stacks_queues.stack_linked_list import StackLinkedList

def test_push_and_pop():
    s = StackLinkedList()
    s.push(10)
    s.push(20)
    s.push(30)
    assert s.peek() == 30
    assert s.pop() == 30
    assert s.peek() == 20
    assert len(s) == 2

def test_empty_stack_errors():
    s = StackLinkedList()
    with pytest.raises(IndexError):
        s.pop()
    with pytest.raises(IndexError):
        s.peek()

def test_is_empty_and_size():
    s = StackLinkedList()
    assert s.is_empty()
    s.push(100)
    s.push(200)
    assert not s.is_empty()
    assert s.size() == 2
