# arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]


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

    # Your code here

    return -1  # not found

print(linear_search(arr1, -6))
# print(binary_search(arr, 0))
