class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1   # Height of node in AVL tree


class AVLTree:
    def insert(self, root, value):
        # 1. Normal BST insertion
        if not root:
            return Node(value)

        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        # 2. Update height
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        # 3. Get balance factor
        balance = self.get_balance(root)

        # 4. Fix violations

        # Case 1: Left Left
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        # Case 2: Right Right
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # Case 3: Left Right
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Case 4: Right Left
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # ---------------- DELETE ---------------- #

    def delete(self, root, value):
        # 1. Standard BST delete
        if not root:
            return root

        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            # node with 1 or 0 children
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # node with 2 children → inorder successor
            successor = self.get_min_value(root.right)
            root.value = successor.value
            root.right = self.delete(root.right, successor.value)

        # 2. Update height
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        # 3. Balance
        balance = self.get_balance(root)

        # Case 1: Left Left
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # Case 2: Left Right
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Case 3: Right Right
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # Case 4: Right Left
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # ---------------- SEARCH ---------------- #

    def search(self, root, value):
        if not root:
            return False
        if root.value == value:
            return True
        if value < root.value:
            return self.search(root.left, value)
        return self.search(root.right, value)

    # ---------------- ROTATIONS ---------------- #

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Rotate
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Rotate
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    # ---------------- UTILITIES ---------------- #

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def get_min_value(self, node):
        while node.left:
            node = node.left
        return node
