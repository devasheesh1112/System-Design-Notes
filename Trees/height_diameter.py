
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    return 1 + max(left_height, right_height)


def diameter(root):
    max_diameter = 0

    def calculate_height(node):
        nonlocal max_diameter

        if node is None:
            return 0

        left_height = calculate_height(node.left)
        right_height = calculate_height(node.right)

        # Diameter measured in edges
        max_diameter = max(
            max_diameter,
            left_height + right_height
        )

        return 1 + max(left_height, right_height)

    calculate_height(root)
    return max_diameter


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Height:", height(root))
    print("Diameter:", diameter(root))
