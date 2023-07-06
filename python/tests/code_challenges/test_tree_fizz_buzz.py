import pytest
from code_challenges.tree_fizz_buzz import fizz_buzz_tree
from data_structures.kary_tree import KaryTree, Node


# @pytest.mark.skip("TODO")
def test_exists():
    assert fizz_buzz_tree


# @pytest.mark.skip("TODO")
def test_one_to_15_fizzy_clone(tree):

    fizzy_tree = fizz_buzz_tree(tree)

    actual = fizzy_tree.breadth_first()

    expected = [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_new_copy_returned(tree):

    fizz_buzz_tree(tree)

    actual = tree.breadth_first()

    expected = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
    ]

    assert actual == expected


@pytest.fixture
def tree():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    nine = Node(9)
    ten = Node(10)
    eleven = Node(11)
    twelve = Node(12)
    thirteen = Node(13)
    fourteen = Node(14)
    fifteen = Node(15)

    """
                            1
                2                       3
            4  5  6               7     8          9
        10  11 12              13            14   15
    """

    one.children = [two, three]
    two.children = [four, five, six]
    three.children = [seven, eight, nine]
    four.children = [ten]
    five.children = [eleven]
    six.children = [twelve]
    seven.children = [thirteen]
    nine.children = [fourteen, fifteen]

    return KaryTree(one)


# Extra tests for expected outcome, expected failure, and edge case

# Expected Outcome, single node

def test_single_node():
    node = Node(7)
    tree = KaryTree(node)
    fizz_buzz_result = fizz_buzz_tree(tree)
    expected = ["7"]
    assert fizz_buzz_result.breadth_first() == expected


# Expected Failure, non-integer values

def test_non_integer_values():
    tree = KaryTree(Node("Hello", [Node("World")]))
    fizzy_tree = fizz_buzz_tree(tree)
    actual = fizzy_tree.breadth_first()
    expected = ["Hello", "World"]
    assert actual == expected


# Edge Case, empty tree

def test_empty_tree():
    tree = KaryTree()
    fizzy_tree = fizz_buzz_tree(tree)
    actual = fizzy_tree.breadth_first()
    assert actual == []
