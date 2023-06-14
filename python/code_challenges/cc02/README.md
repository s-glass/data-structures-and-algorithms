## Code Challenge: Class 02

**Description:**
Create a function called insertShiftArray which takes in an array and a value to be added. Without using built-in methods, return an array with the new value in the middle index.

Created in a group with Dan Quinn, Jared Ciccarello, and Ashley Taylor

* Resource for code construction: (https://stackoverflow.com/questions/48561673/adding-items-in-the-middle-of-a-list-in-python)

### Whiteboard Process

![Code Challenge 02](cc02-whiteboard.png)

### Approach & Efficiency

* This approach defines the list to be added to, creates a function that defines the list midpoint and adds the value to the middle, then prints the function.

* Regarding efficiency, this solution has a time complexity of O(n) since we are
* Big O include a time complexity of 0(n) and space complexity of 0(1).

### Solution

```
list = [ 5, 6, 7, 8 ]
value = 10

def insertShiftArray
     midpoint = len(list) // 2
     list[0:midpoint] + [value] + list[midpoint:]

print insertShiftArray ==> [ 5, 6, 10, 7, 8 ]
```
