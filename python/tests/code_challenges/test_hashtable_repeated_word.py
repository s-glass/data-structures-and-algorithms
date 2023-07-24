import pytest
from code_challenges.hashtable_repeated_word import first_repeated_word


# @pytest.mark.skip("TODO")
def test_blank():
    actual = first_repeated_word("")
    expected = None
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_no_repeat():
    actual = first_repeated_word("nobody here but us chickens")
    expected = None
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_a_a():
    actual = first_repeated_word("apple apple")
    expected = "apple"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_a_b_a():
    actual = first_repeated_word("apple banana apple")
    expected = "apple"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_a_b_a_b():
    actual = first_repeated_word("apple banana apple banana")
    expected = "apple"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_a_b_b_a():
    actual = first_repeated_word("apple banana banana apple")
    expected = "banana"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_ignore_case():
    actual = first_repeated_word("apple banana BANANA apple")
    expected = "banana"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_ignore_case_flipped():
    actual = first_repeated_word("apple BANANA banana apple")
    expected = "banana"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_punctuation():
    actual = first_repeated_word("apple? BANANA! banana, apple.")
    expected = "banana"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_punctuation_joins():
    txt = """
  apple
  apple.apple-apple
  banana
  apple?apple
  banana
  """

    actual = first_repeated_word(txt)
    expected = "banana"
    assert actual == expected


# Adding tests for expected outcome, error, and edge cases

# expected outcome
@pytest.mark.skip("TODO")
def test_multiple_repeats():
    input_str = "apple banana banana apple cherry banana"
    actual = first_repeated_word(input_str)
    expected = "banana"
    assert actual == expected

# no repeated words
@pytest.mark.skip("TODO")
def test_no_repeats():
    input_str = "this is a test string with no repeated words"
    actual = first_repeated_word(input_str)
    expected = None
    assert actual == expected

# single word input string
@pytest.mark.skip("TODO")
def test_one_word():
    input_str = "apple"
    actual = first_repeated_word(input_str)
    expected = None
    assert actual == expected
