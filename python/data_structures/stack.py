from data_structures.invalid_operation_error import InvalidOperationError

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """
   Create a Stack class that has a top property. It creates an empty Stack when instantiated.

   This object should be aware of a default empty value assigned to top when the stack is created.

   The class should contain the following methods:
push
Arguments: value
adds a new node with that value to the top of the stack with an O(1) Time performance.
pop
Arguments: none
Returns: the value from node from the top of the stack
Removes the node from the top of the stack
Should raise exception when called on empty stack
peek
Arguments: none
Returns: Value of the node located at the top of the stack
Should raise exception when called on empty stack
is empty
Arguments: none
Returns: Boolean indicating whether or not the stack is empty.
    """

    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        if self.top is None:
            self.top = node
        else:
         node.next = self.top
         self.top = node

    def pop(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        value = self.top.value
        self.top = self.top.next
        return value


    def peek(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value


    def is_empty(self):
        if self.top is None:
            return True


