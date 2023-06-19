class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"<Node value={self.value}>"
    

def middleNode(linkedList):
    slowNode = linkedList
    fastNode = linkedList
    print("slow node", slowNode)
    print("fast node", fastNode)
    while fastNode.next is not None and fastNode.next is not None:
        slowNode = slowNode.next
        fastNode = fastNode.next.next
    return slowNode


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

    # 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6

    mid = middleNode(first)
    print(mid)

