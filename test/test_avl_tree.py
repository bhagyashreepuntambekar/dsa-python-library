import pytest

from trees.avl_tree import AVLTree


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)


def test_insert_balanced_structure():
    tree = AVLTree()
    root = None

    # This sequence forces rotations
    for v in [10, 20, 30]:
        root = tree.insert(root, v)

    # AVL must rebalance to:
    #        20
    #      /    \
    #     10     30
    assert inorder(root) == [10, 20, 30]
    assert root.value == 20    # check rotation happened


def test_insert_complex_rotations():
    tree = AVLTree()
    root = None

    # LR rotation expected
    for v in [30, 10, 20]:
        root = tree.insert(root, v)

    assert inorder(root) == [10, 20, 30]
    assert root.value == 20    # LR fix


def test_search():
    tree = AVLTree()
    root = None

    for v in [50, 30, 70, 20, 40, 60, 80]:
        root = tree.insert(root, v)

    assert tree.search(root, 40) is True
    assert tree.search(root, 100) is False


def test_delete_leaf_node():
    tree = AVLTree()
    root = None

    for v in [10, 5, 15]:
        root = tree.insert(root, v)

    root = tree.delete(root, 5)

    assert inorder(root) == [10, 15]
    assert tree.search(root, 5) is False


def test_delete_node_with_one_child():
    tree = AVLTree()
    root = None

    for v in [10, 5, 15, 12]:
        root = tree.insert(root, v)

    root = tree.delete(root, 15)

    assert inorder(root) == [5, 10, 12]
    assert tree.search(root, 15) is False


def test_delete_node_with_two_children():
    tree = AVLTree()
    root = None

    for v in [20, 10, 30, 25, 40]:
        root = tree.insert(root, v)

    root = tree.delete(root, 30)

    # 30's inorder successor is 40
    assert inorder(root) == [10, 20, 25, 40]
    assert tree.search(root, 30) is False


def test_tree_remains_balanced_after_many_ops():
    tree = AVLTree()
    root = None

    values = [50, 20, 70, 10, 30, 60, 80, 25, 27, 26]

    for v in values:
        root = tree.insert(root, v)

    # simple check: every node must have balance factor ∈ {-1,0,1}
    def check_balanced(node):
        if not node:
            return True
        bf = tree.get_balance(node)
        return abs(bf) <= 1 and check_balanced(node.left) and check_balanced(node.right)

    assert check_balanced(root) is True
