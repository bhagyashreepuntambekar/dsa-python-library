import pytest
from stacks_queues.stack_array import StackArray

def test_stack_operations():
    s = StackArray()
    assert s.is_empty()

    s.push(10)
    s.push(20)
    s.push(30)
    assert str(s) == "[10, 20, 30]"
    assert s.peek() == 30
    assert s.pop() == 30
    assert s.size() == 2
    assert not s.is_empty()

def test_pop_empty_stack():
    s = StackArray()
    with pytest.raises(IndexError):
        s.pop()

def test_peek_empty_stack():
    s = StackArray()
    with pytest.raises(IndexError):
        s.peek()
