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
        result = ""
        current = self.head
        while current:
            result += str(current.value) + " -> "
            current = current.next
        result += "None"
        return result


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


    def kth_from_end(self, k):
        try:
            if self.head == None:
                return Exception

            else:
                current = self.head
                count = 0
                while current.next:
                    count += 1
                    current = current.next
                difference = count - k

            if k > count:
                raise TargetError

            current_2 = self.head
            for node in range(1, difference + 1):
                current_2 = current_2.next
            return current_2.value
        except Exception as e:
                raise TargetError

# def __str__(self):
#         result = ""
#         current = self.head
#         while current:
#             result += str(current.value) + " -> "
#             current = current.next
#         result += "None"
#         return result

# def zip_lists(list1, list2):
#     current1 = list1.head
#     current2 = list2.head
#     if not current1 and not current2:
#         return None
#     results_LL = LinkedList()
#     while current1 and current2:
#         results_LL.append(current1.value)
#         results_LL.append(current2.value)
#         current1 = current1.next
#         current2 = current2.next
#     while current1:
#         results_LL.append(current1.value)
#         current1 = current1.next
#     while current2:
#         results_LL.append(current2.value)
#         current2 = current2.next
#     return str(results_LL)

class TargetError(Exception):
        pass




#     Write the following method for the Linked List class:
# kth from end
# argument: a number, k, as a parameter.
# Return the node’s value that is k places from the tail of the linked list.
# You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

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


