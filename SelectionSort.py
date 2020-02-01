"""
selection sort scans through the sequence and selects the smallest
thos algorithm maintains both the sorted and unsorted values within the same
sequence structure. Makes multiple passes over the sequence, it only makes a single swap
after each pass
"""

# sorts sequence in ascending order using the selection sort algo
def selectionSort(seq):
    n = len(seq)
    for i in range(n-1):
        # assumption: ith element is the smallest
        small = i
        #determine if any other element contains smaller value
        for j in range(i+1, n):
            if seq[j] < seq[small]:
                small = j
        # swap the ith value and small value only if the smallest is not in position
        if small != i:
            tmp = seq[i]
            seq[i] = seq[small]
            seq[small] = tmp
