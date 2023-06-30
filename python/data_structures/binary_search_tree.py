from data_structures.binary_tree import BinaryTree
from data_structures.binary_tree import Node


class BinarySearchTree(BinaryTree):

    def __init__(self, root=None):
        self.root = root

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._add_recursive(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._add_recursive(current_node.right, value)


    def contains(self, value):
        return self._contains_recursive(self.root, value)

    def _contains_recursive(self, current_node, value):
        if current_node is None:
            return False
        elif value == current_node.value:
            return True
        elif value < current_node.value:
            return self._contains_recursive(current_node.left, value)
        else:
            return self._contains_recursive(current_node.right, value)


'''
Create a Binary Search Tree class
This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
Add
Arguments: value
Return: nothing
Adds a new node with that value in the correct location

Contains
Argument: value
Returns: boolean indicating whether or not the value is in the tree at least once.
'''
