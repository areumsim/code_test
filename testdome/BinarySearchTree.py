### Binary Search Tree

import collections

Node = collections.namedtuple("Node", ["left", "right", "value"])


# 반복문
def contains(root, value):
    while root != None:
        if root.value == value:
            return True

        if root.value > value:
            root = root.left
        else:
            root = root.right
    return False


# 재귀함수
def contains(root, value):
    if root is None:
        return False
    if value == root.value:
        return True
    if value > root.value:
        return contains(root.right, value)
    if value < root.value:
        return contains(root.left, value)


n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)

print(contains(n2, 3))  # True
