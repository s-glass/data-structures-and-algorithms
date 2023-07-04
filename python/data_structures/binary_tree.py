# Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def pre_order(self, values=[]):
        def walk(input_node, value_list):
            if not input_node:
                return
            value_list.append(input_node.value)
            walk(input_node.left, value_list)
            walk(input_node.right, value_list)

        walk(self.root, values)
        return values

    def in_order(self, values=[]):
        def walk(input_node, value_list):
            if not input_node:
                return
            walk(input_node.left, value_list)
            value_list.append(input_node.value)
            walk(input_node.right, value_list)

        walk(self.root, values)
        return values

    def post_order(self, values=[]):
        def walk(input_node, value_list):
            if not input_node:
                return
            walk(input_node.left, value_list)
            walk(input_node.right, value_list)
            value_list.append(input_node.value)

        walk(self.root, values)
        return values

    def find_maximum_value(self):
        # Initialize a variable to store the maximum value.
        max_value = None

        # Set a variable to the root node of the tree.
        node = self.root

        # While the node is not None, do the following:
        while node:

            # If the current value of the node is greater than the current value of the maximum value,
            # update the maximum value.
            if not max_value or node.value > max_value:
                max_value = node.value

            # Set the node to the left child of the current node.
            node = node.left

        # If the maximum value is still None, return -1.
        if max_value is None:
            return -1

        # Otherwise, return the value of the maximum value.
        return max_value
