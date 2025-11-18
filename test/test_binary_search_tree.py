import pytest

from trees.binary_search_tree import BinarySearchTree


def build_sample_bst():
    """
    Build this BST:
            8
          /   \
         3    10
        / \     \
       1   6     14
          / \    /
         4   7  13
    """
    bst = BinarySearchTree()
    for val in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        bst.root = bst._insert(bst.root, val)
    return bst


def test_insert():
    bst = BinarySearchTree()
    bst.root = bst._insert(bst.root, 5)
    bst.root = bst._insert(bst.root, 2)
    bst.root = bst._insert(bst.root, 7)

    assert bst.root.value == 5
    assert bst.root.left.value == 2
    assert bst.root.right.value == 7


def test_search_found():
    bst = build_sample_bst()
    assert bst.search(6) is True
    assert bst.search(14) is True


def test_search_not_found():
    bst = build_sample_bst()
    assert bst.search(100) is False
    assert bst.search(-1) is False


def test_delete_leaf():
    bst = BinarySearchTree()
    for v in [5, 3, 7]:
        bst.root = bst._insert(bst.root, v)

    bst.delete(3)

    assert bst.search(3) is False
    assert bst.root.left is None


def test_delete_node_with_one_child():
    bst = BinarySearchTree()
    for v in [5, 3, 7, 6]:  # 7 has left child 6
        bst.root = bst._insert(bst.root, v)

    bst.delete(7)

    assert bst.search(7) is False
    assert bst.root.right.value == 6   # 6 replaces 7


def test_delete_node_with_two_children():
    bst = build_sample_bst()  # 3 has two children

    bst.delete(3)

    assert bst.search(3) is False
    # After deletion, successor = 4 replaces 3
    assert bst.root.left.value == 4
    assert bst.root.left.right.value in [6, 7]  # subtree still valid
