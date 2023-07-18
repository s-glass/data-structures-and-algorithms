# Blog Notes: Insertion Sort

In the following psudocode, we have two functions that work together to take in an array of integers and return a sorted array, starting from the lowest integer and finishing at the highest integer.

The `Insert` function allows a user to insert an element into a sorted array while maintaining the sorted order.

The `InsertionSort` function uses the `Insert` function to sort the entire array given and returns a fully sorted array.

```python
Insert(int[] sorted, int value)
  initialize i to 0
  WHILE value > sorted[i]
    set i to i + 1
  WHILE i < sorted.length
    set temp to sorted[i]
    set sorted[i] to value
    set value to temp
    set i to i + 1
  append value to sorted

InsertionSort(int[] input)
  LET sorted = New Empty Array
  sorted[0] = input[0]
  FOR i from 1 up to input.length
    Insert(sorted, input[i])
  return sorted
  ```

Let's do a step-through of this process using an example input array:

`[8,4,23,42,16,15]`

Take a look at the visual at the bottom of the blog to follow along.

In the `Insert` function, `i` will traverse the `sorted` array to find the right position the `value` needs to be inserted at. Since the `Insert` function initializes i to 0, let's start at our index value at 0 and take a look at our first `value`, which is 8.

**So, first iteration of `sorted` array is `[8]`.**

This function has two `WHILE` loops. The first will run as long as `value` is greater than the element at index `i` in the sorted array. This loop helps find the correct position for insertion.

Since we only have one value so far, we skip the `WHILE` loops and append 8 to the `sorted` array, and move on to look at the next index value 1, which has a value of `4`.

Since the value 4 is not greater than the existing 8 value, it will do what the first `WHILE` loop tells it to do, and take the `sorted` `i`, which right now is just 8, and add it one index value down the line. It will skip the second `WHILE` loop and append 4 in front of 8.

**The `sorted` array now consists of `[4, 8]`**

It now looks at 23, skips the first loop and uses the second loop to go through the second `WHILE` loop, starting from the index `i` and goeing up to the end of the sorted array.

Inside the loop, 23 will go through a series of switches/swaps to insert `value` into the correct position while shifting any greater elements to the right. Finally, it will append the value to the end of the sorted array.

Since 23 is larger than both 4 and 8, it appends 23 to the end.

**The `sorted` array now consists of `[4, 8, 23]`**

It will run through this process for all of the remining values in the `input` array, including 42, 16, and 15.

**It will stage the `sorted` array to consist of `[4, 8, 15, 16, 23,42]`**


At this point we are only halfway done! We still have our second function
`InsertionSort` to get through.

The `InsertionSort` function will take in an integer array called `input` and returns a new array that is sorted, using the `Insert` function above.

First, it will initialize an empty array and call it `sorted`.

It will then set the first element of the `sorted` array to the first of the `input` array. This step assumes that the first element is already sorted.

Next, it will iterate over the rest of the elements in the `input` array, starting from the second element, and calls the `Insert` function to add each element from the `input` array into the `sorted` array while maintaining the sorted order.

After all the elements from the `input` array have been inserted into the `sorted` array, it will return the finished `sorted` array as the result of the sorted input.

**The returned `sorted` array consists of `[4, 8, 15, 16, 23, 42]`.**


If we wanted to turn this into complete code, we could use the following instead of pseudocode:

```python

Sure! Here's the equivalent Python code for the given pseudocode:

python
Copy code
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
```

![Visual Step-By-Step](/sorting/insertion/cc26-visual.png)
