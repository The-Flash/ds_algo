# O(n) time | O(d) space
def invertBinaryTree(tree):
    if tree is None:
        return
    swapLeftAndRight(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    
if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.left = BinaryTree(2)
    tree.right = BinaryTree(3)
    tree.left.left = BinaryTree(4)
    tree.left.right = BinaryTree(5)
    tree.right.left = BinaryTree(6)
    tree.right.right = BinaryTree(7)
    invertBinaryTree(tree)
    print(tree.left.left.value)
    print(tree.left.right.value)
    print(tree.right.left.value)
    print(tree.right.right.value)
    print(tree.left.value)
    print(tree.right.value)
    print(tree.value) 