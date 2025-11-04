import pytest
from stacks_queues.queue_linked_list import QueueLinkedList

def test_enqueue_dequeue():
    q = QueueLinkedList()
    assert q.is_empty()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    assert str(q) == "[10, 20, 30]"
    assert q.peek() == 10
    assert q.dequeue() == 10
    assert q.peek() == 20
    assert len(q) == 2

def test_dequeue_empty_queue():
    q = QueueLinkedList()
    with pytest.raises(IndexError):
        q.dequeue()

def test_peek_empty_queue():
    q = QueueLinkedList()
    with pytest.raises(IndexError):
        q.peek()
