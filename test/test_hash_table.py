import pytest
from hashtable.hash_table import HashTable


@pytest.fixture
def table():
    """Fixture to create a new HashTable before each test."""
    return HashTable()

def test_put_and_get(table):
    table.put("name", "Alice")
    table.put("age", 25)

    assert table.get("name") == "Alice"
    assert table.get("age") == 25
    assert table.get("nonexistent") is None

def test_update_existing_key(table):
    table.put("age", 25)
    table.put("age", 26)  # should update, not duplicate
    assert table.get("age") == 26
    assert len(table) == 1

def test_remove_key(table):
    table.put("country", "Canada")
    assert table.remove("country") is True
    assert table.get("country") is None
    assert table.remove("country") is False  # removing again returns False

def test_collision_handling():
    # Force collisions by using custom small capacity
    table = HashTable(capacity=2)
    table.put("key1", "A")
    table.put("key2", "B")
    table.put("key3", "C")

    # All should be retrievable even if they collide
    assert table.get("key1") == "A"
    assert table.get("key2") == "B"
    assert table.get("key3") == "C"
    assert len(table) == 3

def test_resize_triggered():
    table = HashTable(capacity=4)
    for i in range(10):
        table.put(f"k{i}", i)
    assert table.capacity >= 8  # resized
    assert len(table) == 10
    for i in range(10):
        assert table.get(f"k{i}") == i
