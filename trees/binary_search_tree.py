class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        self._insert(self.root,value)

    def _insert(self,node,value):
        if node is None:
            node = Node(value)
            return node
        if value < node.value:
            node.left = self._insert(node.left,value)
        else:
          node.right = self._insert(node.right,value)

        return node

    def search(self,value):
        return self._search(self.root,value)

    def _search(self,node,value):
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._search(node.left,value)
        else:
            return self._search(node.right,value)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self,node,value):

        if node is None:
            return None

        if node.value > value:
            node.left =  self._delete(node.left,value)
        if node.value < value:
            node.right =  self._delete(node.right,value)
        if node.value == value:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self.inorder_successor(node.right)
                node.value = successor.value
                node.right = self._delete(node.right,successor.value)
        return node

    def inorder_successor(self,node1):
        while node1 and node1.left is not None:
            node1 = node1.left
        return node1






