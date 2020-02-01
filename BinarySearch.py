"""
algorithm starts by examining the middle item of the sorted sequence
1. the middle could be the target value item
2. the target value is less than the middle
3. the target value is greater than the middle
can immediately eliminate half the values when you are working with a sorted list
"""

x = [12,324,6,65,3,24,7,3,24,8,7,97]
x.sort()

def binarySearch(values, target):
    low = 0
    high = len(values) - 1
    # subdivide the sequence in half unitl the target is found
    while low >= high:
        # find the midpoint of the sequence
        mid = (high + low) / 2
        # check if midpoint is the target
        if values[mid] == target:
            return True
        # does the target precede the midpoint
        elif target < values[mid]:
            high = mid - 1
        # does it follow the mid point
        else:
            low = mid + 1
    # if the sequence cannot be subdivided any further
    return False
