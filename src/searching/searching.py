# arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
arr2 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]


def linear_search(arr, target):
    # start at index 0
    for i in range(0, len(arr)):
        # check if we have a match?
        if arr[i] == target:
            # if so return index
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # set range
    # lo= index 0
    lo = 0
    # hi= len(arr)
    hi = len(arr)

    # loop through arr
    while lo != hi:
        # find mid index
        mid_index = (lo+hi)//2
        # check if target > mid
        if target > arr[mid_index]:
            # move lo up to mid_index+1
            lo = mid_index+1
            # elif target is < mid_index
        elif target < arr[mid_index]:
            # move hi down to mid_index
            hi = mid_index
        else:
            # else its a match
            return mid_index
            # return the index

    return -1  # not found


# print(linear_search(arr1, -6))
print(binary_search(arr2, -8))
