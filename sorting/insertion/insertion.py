
def Insert(sorted_arr, value):
    i = 0
    while value > sorted_arr[i]:
        i += 1
    while i < len(sorted_arr):
        temp = sorted_arr[i]
        sorted_arr[i] = value
        value = temp
        i += 1
    sorted_arr.append(value)

def InsertionSort(input_arr):
    sorted_arr = [input_arr[0]]
    for i in range(1, len(input_arr)):
        Insert(sorted_arr, input_arr[i])
    return sorted_arr
