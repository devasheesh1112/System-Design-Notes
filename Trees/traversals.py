from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root):
    if root is None:
        return

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


def level_order(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Preorder:", end=" ")
preorder(root)

print("\nInorder:", end=" ")
inorder(root)

print("\nPostorder:", end=" ")
postorder(root)

print("\nLevel Order:", end=" ")
level_order(root)