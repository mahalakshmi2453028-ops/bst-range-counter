class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def getcount(root, low, high):
    if root is None:
        return 0

    if low <= root.data <= high:
        return 1 + getcount(root.left, low, high) + getcount(root.right, low, high)
    elif root.data < low:
        return getcount(root.right, low, high)
    else:
        return getcount(root.left, low, high)


root = Node(10)
root.left = Node(5)
root.right = Node(50)
root.right.left = Node(40)
root.right.right = Node(100)

low = 5
high = 40

print("Count of nodes in range:", getcount(root, 5, 40))
