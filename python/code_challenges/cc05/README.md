## Code Challenge: Class 05

**Description:**
* Create a node class with properties for value stored in node and pointer to next node.

* Create a linked list class with head property linked list created upon instantiation with the following methods:

(1) insert
 - artuments: value
 - returns: nothing
 - adds new node with that value to the head of the list, with an O(1) Time performance

(2) includes
 - arguments: value
 - returns: boolean; indicates whether that value exists as a node's value somewhere in the list

(3) to string
 - arguments: none
 - returns: string representing all values in the Linked List, formatted as

Created with Dan Quinn, Anthony Sinitsa, Jared Ciccarello

The 4 tests at the bottom came from a comparison/review of tests prompted from AI via Bard & Chat GPT.

### Whiteboard Process

No whiteboard for this assignment.

### Approach & Efficiency

* This approach creates node and linked list classes which includes the following methods (1) insert, (2) includes, and (3) to string.

* Big O include a time complexity of 0(1) and space complexity of 0(1).


### How to initialize/run the code tests

pytest tests/data_structures/test_linked_list.py

### Solution

```
class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next

class LinkedList:
    def __init__(self, head=None, values=None, insert=None):
        self.head = None


    def insert(self, value):
        self.head = Node(value, self.head)

    def __str__(self):
        if self.head == None:
         return "NULL"
        else:
            current = self.head
            output = ""
            while current:
                output += f"{{ {current.value} }} -> "
                current = current.next
            output += "NULL"
            return output


    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

class TargetError:
    pass
```
