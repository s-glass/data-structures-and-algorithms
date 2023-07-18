# Testing first function, MergeSort

@pytest.mark.skip("TODO")
def test_mergesort_happy_path():
    arr = [38, 27, 43, 3, 9, 82, 10]
    expected_output = [3, 9, 10, 27, 38, 43, 82]
    MergeSort(arr)
    assert arr == expected_output

@pytest.mark.skip("TODO")
def test_mergesort_edge_case():
    arr = [5]
    expected_output = [5]
    MergeSort(arr)
    assert arr == expected_output

@pytest.mark.skip("TODO")
def test_mergesort_error_case():
    arr = None
    try:
        MergeSort(arr)
    except TypeError as e:
        assert str(e) == "'NoneType' object has no attribute 'length'"

# Testing second function, Merge

@pytest.mark.skip("TODO")
def test_merge_happy_path():
    left = [3, 9, 27]
    right = [10, 38, 43, 82]
    arr = [0] * (len(left) + len(right))
    expected_output = [3, 9, 10, 27, 38, 43, 82]
    Merge(left, right, arr)
    assert arr == expected_output

@pytest.mark.skip("TODO")
def test_merge_edge_case():
    left = [1]
    right = [2]
    arr = [0] * (len(left) + len(right))
    expected_output = [1, 2]
    Merge(left, right, arr)
    assert arr == expected_output

@pytest.mark.skip("TODO")
def test_merge_error_case():
    left = [1, 2]
    right = [3, 4]
    arr = [0] * (len(left) + len(right) - 1)  # Error: arr length is not enough for merged result
    try:
        Merge(left, right, arr)
    except IndexError as e:
        assert str(e) == "list assignment index out of range"

