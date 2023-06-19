class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"<Node value={self.value}>"
    
def middleNode(linkedlist: Node):
    count = 0
    currentNode = linkedlist
    while currentNode is not None:
        count += 1
        currentNode = currentNode.next
    middleNode = linkedlist
    for _ in range(count // 2):
        middleNode = middleNode.next
    return middleNode