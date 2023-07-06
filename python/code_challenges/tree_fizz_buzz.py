# from data_structures.binary_tree import BinaryTree

class KaryTree:
    def __init__(self, root=None):
        self.root = root

    def breadth_first(tree):
        list = []
        queue = []
        if tree.root:
            queue.append(tree.root)
        while queue:
            node = queue.pop(0)
            list.append(node.value)
            for child in node.children:
                queue.append(child)
        return list

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []


def fizz_buzz_tree(tree):
    def process_node(node):
        if node is None:
            return None

        new_value = process_value(node.value)
        new_children = [process_node(child) for child in node.children]

        return Node(new_value, new_children)

    def process_value(value):
        divisible_by_3 = value % 3 == 0
        divisible_by_5 = value % 5 == 0

        if divisible_by_3 and divisible_by_5:
            return "FizzBuzz"
        elif divisible_by_3:
            return "Fizz"
        elif divisible_by_5:
            return "Buzz"
        else:
            return str(value)

    new_root = process_node(tree.root)
    new_tree = KaryTree(new_root)
    return new_tree
