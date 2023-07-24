# class Hashtable:
#     def __init__(self, size=100): # takes size to set size of hashtable, if no size, default is 100
#         self.size = size
#         self.table = [None] * self.size # self.table is a list that stores key-value pairs. It has self.size number of elements and all are set to None.

#     def _hash_function(self, key): # calculates hash value for a given key.
#         hash_value = 0
#         for char in key:
#             hash_value += ord(char) # takes characters one by one and gets ASCII value, then adds them to get hash_value
#         return hash_value % self.size  # hash_value taken modulo of self.size to map to an index within the range of the table.

# # set: Arguments: key, value / Returns: nothing
# # This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
# # Should a given key already exist, replace its value from the value argument given to this method.

#     def set(self, key, value):  # sets key-value pair in the hashtable
#         index = self._hash_function(key) # get index calc by using _hash_function for given key

#         # Check if the key already exists at the same index - that self.table[index] is not None, and if key matches key at index.
#         if self.table[index] and self.table[index][0] == key:
#             self.table[index] = (key, value)  # if yes, update existing key-value pair with new value and overwrite previous value
#         else:
#             # Find the next available slot using linear probing.
#             while self.table[index] is not None and self.table[index][0] != key: # if key doesn't already exist at given index, find next open bucket in hashtable. Linear probing: increment index by 1 using modulo self.size until you get to a bucket with value None.
#                 index = (index + 1) % self.size

#             # Set the key-value pair at the available slot.
#             self.table[index] = (key, value)

# # get: Arguments: key / Returns: Value associated with that key in the table

#     def get(self, key): # retrieves value associated with a key from the hashtable
#         index = self._hash_function(key) # calc index using _hash_function for a given key
#         while self.table[index]:
#             if self.table[index][0] == key: # linear probing to search for key in hashtable. Start at index and increment index by 1 until you find the key or reach empty bucket with None.
#                 return self.table[index][1] # return value if key is found in the table
#             index = (index + 1) % self.size
#         raise KeyError(f"Key '{key}' does not exist in the table.") # if you reach an empty slot, key doesn't already exist, so raise error.

# #has: Arguments: key / Returns: Boolean, indicating if the key exists in the table already.

#     def has(self, key): # checks if key exists in table
#         index = self._hash_function(key) # calcs index using _hash_function for given key
#         while self.table[index]:
#             if self.table[index][0] == key: # linear probing to search for key in hashtable; if key is found, return true.
#                 return True
#             index = (index + 1) % self.size
#         return False # if key not found in any existing buckets, return false

# #keys: Returns: Collection of keys

#     def keys(self): # returns list of keys present in table and iterates through each item in the
#         keys = [] # empty list to store keys from table
#         for item in self.table: # iterate through every element in self.table - the list that holds the key-value pairs in the table
#             if item: # checks if item is not None.
#                 keys.append(item[0]) # if not none, it means there's a key-value pair there and you can then get the key from the item, so append key to the keys list
#         return keys #

# # hash: Arguments: key / Returns: Index in the collection for that key


#     def hash(self, key): # allows you to calc hash value for a given key. Calls _hash_function to do the calculation.
#         return self._hash_function(key)


# if __name__ == '__main__':

#     hash1 =  Hashtable()
#     print(hash1.size)
#     print(hash1.hash('super'))









class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None


class Hashtable:
  def __init__(self, size=1024):
    self.size = size
    self._buckets = [None] * size

  def hash(self, key):
    """_summary_

    Args:
        key (_type_): _description_

    Returns:
        _type_: _description_
    """
    return hash(key) % self.size

  def set(self, key, value):
    """_summary_

    Args:
        key (_type_): _description_
        value (_type_): _description_
    """
    index = self.hash(key)

    if self._buckets[index] is None:
      self._buckets[index] = Node(key, value)
    else:
      current = self._buckets[index]
      while current:
        if current.key == key:
          current.value = value
          return
        if current.next is None:
          break
        current = current.next

      new_node = Node(key, value)
      print(new_node)
      current.next = new_node


  def get(self, key):
    """_summary_

    Args:
        key (_type_): _description_

    Raises:
        KeyError: _description_

    Returns:
        _type_: _description_
    """
    index = self.hash(key)

    current = self._buckets[index]
    while current:
      if current.key == key:
        print(current.value)
        return current.value
      current = current.next

    raise KeyError(key)

  def has(self, key):
    """_summary_

    Args:
        key (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
      self.get(key)
      return True
    except KeyError:
      return False

  def keys(self):
    """_summary_

    Returns:
        _type_: _description_
    """
    keys_list = []
    for node in self._buckets:
      current = node
      while current:
        keys_list.append(current.key)
        current = current.next
    return keys_list

  def contains(self, key):
    """
    Args: key (_type_): _description_
    Returns: _type_: _description_
    """
    index = self.hash(key)
    current = self._buckets[index]
    while current:
      if current.key == key:
        return True
      current = current.next
    return False







