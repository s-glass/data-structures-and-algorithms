from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable


def tree_intersection(tree_a, tree_b): # define tree_intersection function and takes in two trees as input
    tree_a_values = set(tree_a.in_order()) #pulls values of nodes in tree A by doing in-order traversal, returns list of values in order converted into a set to remove duplicates
    tree_b_values = set(tree_b.in_order()) #does the same for tree B

    hashmap = Hashtable() # brings in hashtable class
    common_values_list = [] # creates an empty list to hold common values in both trees

    for value in tree_a_values: # iterate through each tree A value
        hashmap.set(value, True) # for each value, store value as key in hashtable with value of True - shows it is present

    for value in tree_b_values: # iterate through each tree B value
        if hashmap.has(value): # Check hashmap if the value is already present
            common_values_list.append(value) # if the value is already in hashmap, it means value exists in both trees, so append common_values_list

    return common_values_list # return common_values_list
