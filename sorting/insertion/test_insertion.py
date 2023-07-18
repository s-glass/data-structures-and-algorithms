# Testing first function, Insert
# @pytest.mark.skip("TODO")
def test_insertion(self):
  # Test case 1
  arr1 = [1, 3, 5, 7, 9]
  Insert(arr1, 4)
  self.assertEqual(arr1, [1, 3, 4, 5, 7, 9])

  # Test case 2
  arr2 = [2, 4, 6, 8]
  Insert(arr2, 10)
  self.assertEqual(arr2, [2, 4, 6, 8, 10])

  # Test case 3
  arr3 = [15, 20, 25, 30]
  ImportErrornsert(arr3, 18)
  self.assertEqual(arr3, [15, 18, 20, 25, 30])

  # Test case 4 (Empty array)
  arr4 = []
  Insert(arr4, 5)
  self.assertEqual(arr4, [5])



# Testing second function, Insert Sort
# @pytest.mark.skip("TODO")
def test_sorting(self):
  # Test case 1
  arr1 = [8, 4, 23, 42, 16, 15]
  sorted_arr1 = InsertionSort(arr1)
  self.assertEqual(sorted_arr1, [4, 8, 15, 16, 23, 42])

  # Test case 2
  arr2 = [3, 1, 7, 5, 4, 2, 6]
  sorted_arr2 = InsertionSort(arr2)
  self.assertEqual(sorted_arr2, [1, 2, 3, 4, 5, 6, 7])

  # Test case 3 (Empty array)
  arr3 = []
  sorted_arr3 = InsertionSort(arr3)
  self.assertEqual(sorted_arr3, [])

  # Test case 4 (Array with a single element)
  arr4 = [9]
  sorted_arr4 = InsertionSort(arr4)
  self.assertEqual(sorted_arr4, [9])

  # Test case 5 (Already sorted array)
  arr5 = [1, 2, 3, 4, 5]
  sorted_arr5 = InsertionSort(arr5)
  self.assertEqual(sorted_arr5, [1, 2, 3, 4, 5])



