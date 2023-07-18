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

# Example:
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    MergeSort(arr)
    print(arr)
# Output: [3, 9, 10, 27, 38, 43, 82]
