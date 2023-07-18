# Blog Notes: Merge Sort

In the following psudocode, we have two functions that work together to take in an array of integers and return the array in ascending order. The code divides the array into smaller subarrays, sorts them, and migrates them back together into a final sorted array.

The `MessageSort` function calculates the midpoint of the array it takes in, divides the array into left (elements from 0-mid-1) and right (elements from mid to n-1). It then calls the MergeSort function recursively on both left and right to sort them, and then calls Merge to the sorted L and R subarrays back into the original array.

The `Merge` function uses variables i, j, and k to track positions in L, R, and arr. It then loops through L and R comparing elements from both and then places them in the right order in the arr. If element in L is less or equal to element in R, it puts element from L into the `k` position in the array, then increments i and k. If not, it does the same with the element from R and increments j and k. After looping, it checks if there are any elements left, and if so, appends remaining elements to the end of arr.

```python
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
  ```

Let's do a step-through of this process using an example input array:

`[8,4,23,42,16,15]`

![Visual Step-By-Step image](/sorting/insertion/cc27-visual1.png)

![Visual Step-By-Step table](/sorting/insertion/cc27-visual2.png)


If we wanted to turn this into complete code, we could use the following instead of pseudocode:

```python
def MergeSort(arr):
    n = len(arr)
    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]
        MergeSort(left)
        MergeSort(right)
        Merge(left, right, arr)

def Merge(left, right, arr):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
```
