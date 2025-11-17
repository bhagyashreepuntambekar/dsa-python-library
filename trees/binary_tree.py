from collections import deque


class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.index = None
        self.root = None

    def build_binary_tree(self,preorder):
        if self.index >= len(preorder):
            return None

        value = preorder[self.index]
        self.index += 1
        if value == -1:
            return None

        node = Node(value)
        node.left = self.build_binary_tree(preorder)
        node.right = self.build_binary_tree(preorder)

        return node

    def preorder_traversal(self,root:Node):
        if root is None:
            return

        print(root.value)
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)

    def inorder_traversal(self,root:Node):
        if root is None:
            return

        self.inorder_traversal(root.left)
        print(root.value)
        self.inorder_traversal(root.right)

    def postorder_traversal(self,root:Node):
        if root is None:
            return

        self.postorder_traversal(root.left)
        self.postorder_traversal(root.right)
        print(root.value)

    def levelorder_traversal(self,root:Node):
        if root is None:
            return
        queue = deque([root,None])

        while queue:
            curr_node = queue.popleft()
            if curr_node is None:
                print()
                if queue:
                    queue.append(None)
            else:
                print(curr_node.value,end=" ")
                if curr_node.left is not None:
                    queue.append(curr_node.left)
                if curr_node.right is not None:
                    queue.append(curr_node.right)

    def insert(self,value):
        new_node = value
        queue = deque([self.root])

        while queue:
            current = queue.popleft()
            if current.left is None:
                current.left = new_node
                break
            else:
                queue.append(current.left)
            if current.right is None:
                current.right = new_node
                break
            else:
                queue.append(current.right)

    def search(self,value):
        queue = deque([self.root])

        while queue:
            current = queue.popleft()
            if current.value == value:
                return True
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return False

    def delete(self,value):
        if not self.root:
            return None

        queue = deque([self.root])

        node_to_delete = None
        parent_of_last = None
        last_node = None

        while queue:
            last_node = queue.popleft()
            if last_node.value == value:
                node_to_delete = last_node

            if last_node.left:
                parent_of_last = last_node
                queue.append(last_node)
            if last_node.right:
                parent_of_last = last_node
                queue.append(last_node.right)

        if not node_to_delete:
            return False

        node_to_delete.value = last_node.value

        if parent_of_last.right == last_node:
            parent_of_last.right = None
        else:
            parent_of_last.left = None

        return True






