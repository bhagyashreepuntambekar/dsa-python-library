import pytest

from trees.binary_tree import BinaryTree, Node


@pytest.fixture
def sample_tree():
    tree = BinaryTree()
    tree.index = 0
    preorder = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, -1]
    tree.root = tree.build_binary_tree(preorder)
    return tree

def test_build_binary_tree(sample_tree):
    assert sample_tree.root.value == 1
    assert sample_tree.root.left.value == 2
    assert sample_tree.root.right.value == 3
    assert sample_tree.root.left.left.value == 4
    assert sample_tree.root.left.right.value == 5

def test_preorder_traversal(sample_tree,capsys):
    sample_tree.preorder_traversal(sample_tree.root)
    captured = capsys.readouterr().out.strip().split('\n')
    assert list(map(int,captured)) ==[4, 5, 2, 3, 1]
def test_inorder_traversal(sample_tree, capsys):
    sample_tree.inorder_traversal(sample_tree.root)
    captured = capsys.readouterr().out.strip().split('\n')
    assert list(map(int, captured)) == [4, 2, 5, 1, 3]


def test_postorder_traversal(sample_tree, capsys):
    sample_tree.postorder_traversal(sample_tree.root)
    captured = capsys.readouterr().out.strip().split('\n')
    assert list(map(int, captured)) == [4, 5, 2, 3, 1]


def test_levelorder_traversal(sample_tree, capsys):
    sample_tree.levelorder_traversal(sample_tree.root)
    captured = capsys.readouterr().out.strip().split()
    assert list(map(int, captured)) == [1, 2, 3, 4, 5]


def test_search(sample_tree):
    assert sample_tree.search(4) is True
    assert sample_tree.search(99) is False


def test_insert(sample_tree):
    new_node = Node(6)
    sample_tree.insert(new_node)
    assert sample_tree.root.left.left.left == new_node or sample_tree.root.left.left.right == new_node \
        or sample_tree.root.left.right.left == new_node or sample_tree.root.left.right.right == new_node \
        or sample_tree.root.right.left == new_node or sample_tree.root.right.right == new_node


def test_delete(sample_tree):
    assert sample_tree.delete(5) is True
    assert sample_tree.search(5) is False
    # Deleting non-existent node
    assert sample_tree.delete(99) is False
