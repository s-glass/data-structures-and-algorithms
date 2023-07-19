import pytest
from merge import MergeSort, Merge

# empty array
# array of one
# array with duplicates


# Testing first function, MergeSort

@pytest.mark.skip("TODO")
def test_mergesort_empty_array():
    arr = []
    expected_output = []
    MergeSort(arr)
    assert arr == expected_output

@pytest.mark.skip("TODO")
def test_mergesort_single_item():
    arr = [5]
    expected_output = [5]
    MergeSort(arr)
    assert arr == expected_output

@pytest.mark.skip("TODO")
def test_mergesort_duplicates():
    arr = [38, 27, 43, 3, 9, 27, 10, 3]
    expected_output = [3, 3, 9, 10, 27, 27, 38, 43]
    MergeSort(arr)
    assert arr == expected_output



# Testing second function, Merge

@pytest.mark.skip("TODO")
def test_merge_empty_array():
    left = []
    right = []
    arr = [0] * (len(left) + len(right))
    expected_output = []
    Merge(left, right, arr)
    assert arr == expected_output

@pytest.mark.skip("TODO")
def test_merge_single_item():
    left = [1]
    right = []
    arr = [0] * (len(left) + len(right))
    expected_output = [1]
    Merge(left, right, arr)
    assert arr == expected_output

@pytest.mark.skip("TODO")
def test_merge_duplicates():
    left = [1, 3, 9]
    right = [3, 10, 27]
    arr = [0] * (len(left) + len(right))
    expected_output = [1, 3, 3, 9, 10, 27]
    Merge(left, right, arr)
    assert arr == expected_output

