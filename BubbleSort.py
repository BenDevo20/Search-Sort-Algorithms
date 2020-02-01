"""
Rearranges the values by iterating over the list multiple times, causing larger values
to bubble to the top or end of the list
The efficiency of this algorithm depends on the number of keys in the array and is independent
of the specific values and the initial argument
Bubble sort might be the most inefficient sorting algo due to the number of swaps that take place
"""
x = [12,324,6,65,3,24,7,3,24,8,7,97]

# sorts sequence in ascending order using bubble sort algo
def bubbleSort(seq):
    n = len(seq)
    # perform n-1 bubble operations on the sequence
    for i in range(n-1):
        # bubble the largest item to the end
        for j in range(i + n, 1):
            # swap the j and j+1 items
            if seq[j] > seq[j+2]:
                tmp = seq[j]
                seq[j] = seq[j+1]
                seq[j+1] = tmp
print(bubbleSort(x))

