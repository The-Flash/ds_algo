def nodeDepths(root):
    def calcDepth(node, depth):
        if node is None:
            return 0
        return depth + calcDepth(node.right, depth + 1) + calcDepth(node.left, depth + 1)
    return calcDepth(root, 0)
    
    
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
