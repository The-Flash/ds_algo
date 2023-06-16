class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"<Node value={self.value}>"

def removeDuplicatesFromLinkedList(head: Node):
    # current node points to the start of the linked list
    currentNode = head
    # should stop when we meet the tail end which will be None
    while currentNode is not None:
        # check if the next node is different for the current node
        nextDistinctNode = currentNode.next
        # while it is not different keep comparing the next value
        while (nextDistinctNode is not None 
               and 
               nextDistinctNode.value == currentNode.value):
            nextDistinctNode = nextDistinctNode.next
        # if we get here, then that means the next value is distinct
        # so we remove all the nodes in-between
        currentNode.next = nextDistinctNode
        # currentNode should now point to the nextDistinctNode
        currentNode = nextDistinctNode
    return head

def linkedListPrinter(head: Node):
    currentNode = head
    values = []
    while currentNode is not None:
        values.append(str(currentNode))
        currentNode = currentNode.next
    return values

if __name__ == "__main__":
    first = Node(1)
    second = Node(1)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(4)
    sixth = Node(4)
    seventh = Node(5)
    eight = Node(6)
    ninth = Node(6)
    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seventh
    seventh.next = eight
    eight.next = ninth

    print(linkedListPrinter(first))
    removeDuplicatesFromLinkedList(first)
    print(linkedListPrinter(first))