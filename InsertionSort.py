"""
insertion sort maintains a collection of sorted items and a collection of items to be sorted
algorithms maintains borth the sorted and unsorted collections within the same sequence structure
list sorted values at the front of the sequence and picks the next unsorted value from the first
of those yet to be positioned
"""
x = [12,324,6,65,3,24,7,3,24,8,7,97]
# sorts a sequence in ascending order using the inserion sort algo
def insertionSort(seq):
    n = len(seq)
    # first item as the only sorted entry -- starting point
    for i in range(1, n):
        # save the value to be positioned
        value = seq[i]
        # find the position where value fits in the ordered part of the list
        pos = i
        while pos > 0 and value < seq[pos - 1]:
            # shift items to the right during the search
            seq[pos] = seq[pos - 1]
            pos -= 1
        # save values into the open slot
        seq[pos] = value
print(insertionSort(x))
