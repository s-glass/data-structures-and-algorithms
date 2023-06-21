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


    # append arguments: new value, adds new node with given value to the end of the list
    #if/else added with search from chat GPT

    def append(self, value):
         new_node = Node(value)
         if self.head is None:
            self.head = new_node
         else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # insert before arguments: value, new value
    # adds new node with given new value immediately before the first node that has the value specified

    def insert_before(self, value, new_value):
        try:
            new_node = Node(new_value)
            if self.head and self.head.value == value:
                new_node.next = self.head
                self.head = new_node
            current = self.head
            while current.next.value != value:
                current = current.next
            temp = current.next
            current.next = new_node
            new_node.next = temp
        except Exception as e:
            raise TargetError

    # insert after arguments: value, new value
    # adds new node with given new value immediately after first node that has the value specified

    def insert_after(self, value, new_value):
        try:
            new_node = Node(new_value)
            current = self.head
            while current.value != value:
                current = current.next
            temp = current.next
            current.next = new_node
            new_node.next = temp
        except Exception as e:
            raise TargetError



class TargetError(Exception):
    pass


"""
Create a node class with properties for value stored in node and pointer to next node.
"""

"""
Create a linked list class
- with head property
- linked list created upon instantiation
    """

"""""
## (1) insert
 - artuments: value
 - returns: nothing
 - adds new node with that value to the head of the list, with an O(1) Time performance
"""

"""
# (2) includes
# - arguments: value
# - returns: boolean; indicates whether that value exists as a node's value somewhere in the list
"""
"""
# (3) to string
# - arguments: none
# - returns: string representing all values in the Linked List, formatted as
"""


