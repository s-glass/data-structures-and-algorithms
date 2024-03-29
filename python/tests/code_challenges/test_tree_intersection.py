import pytest
from code_challenges.tree_intersection import tree_intersection
from data_structures.binary_tree import BinaryTree, Node
from data_structures.queue import Queue


def test_exists():
    assert tree_intersection


@pytest.mark.skip("TODO")
def test_tree_intersection():

    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [125, 175, 100, 160, 500, 200, 350]

    assert sorted(actual) == sorted(expected)

@pytest.mark.skip("TODO")
def add_values_to_empty_tree(tree, values):
    """
    Helper function to add given values to BinaryTree
    """
    tree.root = Node(values.pop())
    q = Queue()

    q.enqueue(tree.root)

    while values:
        node = q.dequeue()
        node.left = Node(values.pop())
        node.right = Node(values.pop()) if values else None
        q.enqueue(node.left)
        q.enqueue(node.right)

# add 3 tests per function

# Happy Path
@pytest.mark.skip("TODO")
def test_tree_intersection_happy_path():
    # Create two binary trees with common values
    tree_a = BinaryTree()
    values_a = [5, 2, 8, 1, 4, 6, 9]
    add_values_to_empty_tree(tree_a, values_a)

    tree_b = BinaryTree()
    values_b = [2, 1, 7, 4, 6, 9]
    add_values_to_empty_tree(tree_b, values_b)

    # Expected common values: [1, 2, 4, 6, 9]
    expected = [1, 2, 4, 6, 9]
    assert sorted(tree_intersection(tree_a, tree_b)) == sorted(expected)

# Edge Case
@pytest.mark.skip("TODO")
def test_tree_intersection_edge_case():
    # Create two binary trees with only one node (same value)
    tree_a = BinaryTree()
    tree_a.root = Node(5)

    tree_b = BinaryTree()
    tree_b.root = Node(5)

    # Expected common value: [5]
    expected = [5]
    assert tree_intersection(tree_a, tree_b) == expected


# Error Case
@pytest.mark.skip("TODO")
def test_tree_intersection_error_case():
    # Test with one of the binary trees being None
    tree_a = BinaryTree()
    values_a = [5, 2, 8]
    add_values_to_empty_tree(tree_a, values_a)

    # The second binary tree is None
    tree_b = None

    # Expected common values: []
    assert tree_intersection(tree_a, tree_b) == []

    # Test with invalid data types as input
    tree_c = BinaryTree()
    values_c = [5, 2, 8]
    add_values_to_empty_tree(tree_c, values_c)

    # Pass a string instead of a binary tree as the second parameter
    invalid_input = "not a binary tree"

    # We can expect the function to raise an appropriate exception when invalid data types are provided
    with pytest.raises(Exception):
        tree_intersection(tree_c, invalid_input)
