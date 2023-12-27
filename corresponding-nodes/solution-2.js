function correspondingNodes(tree1, tree2, node1) {
    const path = []
    let currNode = node1;
    while (currNode !== tree1) {
        const parent = currNode.parentNode;
        const currIndex = Array.from(parent.children).indexOf(currNode);
        path.push(currIndex)
        currNode = parent;
    }

    return path.reduceRight((foundNode, childIndex) => {
        return foundNode.children[childIndex];
    });
}