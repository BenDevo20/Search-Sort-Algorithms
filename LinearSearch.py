"""
Demonstrates the different kinds of linear search functions in python
"""
import numpy as np

x = [45,23,29,10,28,567]

# searches for defined element in unsorted list
def linearSearch(Values, target):
    n = len(Values)
    for i in range(n):
        # return true if the target is in values
        if Values[i] == target:
            return True
    return False
print(linearSearch(x,23))

# linear search on a sorted list - check if the next number is greater than the previous
def sortedLinearSearch(values,item):
    n = len(values)
    for i in range(n):
        # if the item is found return true
        if values[i] == item:
            return True
        # if target is larger than the ith element -- not in sequence
        elif values[i] > item:
            return False
    return False

# finds smallest value in a unsorted list
def findSmallest(values):
    n = len(values)
    # assume the first item in the list is smallest
    smallest = values[0]
    # find any item in sequence smaller than initial point
    for i in range(1,n):
        if x[i] < smallest:
            smallest = values[i]
    return smallest

print(findSmallest(x))

