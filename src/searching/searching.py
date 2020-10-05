
# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start=0, end=None):
    if len(arr) < 1:
        return -1
    if end:
        #if endpoint has been set
        middle = (start + end) // 2
    else:
        #if endpoint has not been set
        middle = (len(arr) + start) // 2
    if arr[middle] == target:
        return middle
    elif arr[middle] > target:
        return binary_search(arr, target, start = 0, end = middle)
    else:
        return binary_search(arr, target, start = middle)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass

