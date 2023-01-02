class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

"""
[]
        a
      /   \
     b     c
    / \     \
   d   e      f
"""

# def depthFistValues(root):
#     if root is None:
#         return []
#     result = []
#     stack = [root]
#     while(len(stack) > 0):
#         current = stack.pop()
#         result.append(current.val)
#         if current.right:
#             stack.append(current.right)
#         if current.left:
#             stack.append(current.left)
#     return result


def depthFistValues(root):
    if root is None:
        return []
    leftValues = depthFistValues(root.left)
    rightValues = depthFistValues(root.right)
    return [root.val, *leftValues, *rightValues]
print(depthFistValues(a))