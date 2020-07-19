# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    if len(arr) < 1:
        return []
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        # j gets the very next index after the current index
        j = cur_index+1
        while j <= len(arr)-1:
            if arr[j] < arr[smallest_index]:
                smallest_index = j
            j += 1
        # TO-DO: swap
        # Your code here
        # store the next smallest index we found
        nextSmall= arr[smallest_index]
        # move the j index to current index position
        arr[smallest_index] = arr[cur_index]
        # move smallest index to current index
        arr[cur_index] = nextSmall

    return arr

#      0  1  2  3  4  5  6  7  8  9
# arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(selection_sort(arr))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # return empty arr if input is empty
    if len(arr) < 1:
        return []
    # make 'i' an int
    end_index= len(arr)-1
    while end_index > 0:
        for i in range(0, end_index):
            cur_index= i
            next_index= i+1
            if arr[cur_index] > arr[next_index]:
                swap= arr[cur_index]
                arr[cur_index]= arr[next_index]
                arr[next_index]= swap
        end_index-= 1
        

    return arr

# print(bubble_sort(arr))


'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
