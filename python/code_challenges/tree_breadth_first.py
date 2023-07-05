# from data_structures.binary_tree import BinaryTree, Node


def breadth_first(tree):
    list = []
    queue = []

    if tree.root:
        queue.append(tree.root)

    while queue:
        node = queue.pop(0)
        list.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return list
