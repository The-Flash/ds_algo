package main

import "fmt"

type Node struct {
	data int
}

func NewNode(data int) Node {
	return Node{
		data: data,
	}
}

type BinaryTree struct {
	value Node
	left  *BinaryTree
	right *BinaryTree
}

func NewBinaryTree(v Node, l *BinaryTree, r *BinaryTree) *BinaryTree {
	return &BinaryTree{
		value: v,
		left:  l,
		right: r,
	}
}

func TraverseTree(tree *BinaryTree) {
	queue := []*BinaryTree{tree}
	for {
		if len(queue) == 0 {
			break
		}

		current := queue[len(queue)-1]
		queue = queue[:len(queue)-1]

		if current == nil {
			continue
		}

		fmt.Println(current.value)
		queue = append(queue, current.left, current.right)
	}
}

func InvertBinaryTree(tree *BinaryTree) {
	queue := []*BinaryTree{tree}
	for {
		if len(queue) == 0 {
			break
		}
		// pop item from queue
		current := queue[len(queue)-1]
		queue = queue[:len(queue)-1]

		if current == nil {
			continue
		}
		// Swap left and right sub trees
		current.right, current.left = current.left, current.right
		queue = append(queue, current.left, current.right)
	}
}

func main() {
	tree := NewBinaryTree(
		NewNode(1),
		NewBinaryTree(
			NewNode(4),
			NewBinaryTree(
				NewNode(2),
				NewBinaryTree(
					NewNode(3),
					nil,
					nil,
				),
				NewBinaryTree(
					NewNode(6),
					nil,
					nil,
				),
			),
			NewBinaryTree(
				NewNode(5),
				nil,
				nil,
			),
		),
		NewBinaryTree(
			NewNode(6),
			NewBinaryTree(
				NewNode(7),
				nil,
				nil,
			),
			NewBinaryTree(
				NewNode(8),
				nil,
				nil,
			),
		),
	)
	fmt.Println(".....Before....")
	// TraverseTree(tree)
	fmt.Println(tree.value)
	fmt.Println(tree.left.value)
	fmt.Println(tree.right.value)
	fmt.Println(tree.left.left.value)
	fmt.Println(tree.left.right.value)

	InvertBinaryTree(tree)

	fmt.Println(".....After....")
	fmt.Println(tree.value)
	fmt.Println(tree.left.value)
	fmt.Println(tree.right.value)
	fmt.Println(tree.left.left.value)
	fmt.Println(tree.left.right.value)

}
