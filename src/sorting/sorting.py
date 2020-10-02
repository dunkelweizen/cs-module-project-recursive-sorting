# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    if elements == len(arrA):
        return arrA
    if elements == len(arrB):
        return arrB

    pointerA = 0
    pointerB = 0
    merge_pointer = 0
    while pointerA < len(arrA) and pointerB < len(arrB):
        if arrA[pointerA] < arrB[pointerB]:
            merged_arr[merge_pointer] = arrA[pointerA]
            pointerA += 1
            merge_pointer += 1
        if arrA[pointerA] > arrB[pointerB]:
            merged_arr[merge_pointer] = arrB[pointerB]
            pointerB += 1
            merge_pointer += 1

    if pointerA != len(arrA) - 1:
        for element in arrA[pointerA:]:
            merged_arr[merge_pointer] = element
            merge_pointer += 1
    elif pointerB != len(arrB) - 1:
        for element in arrB[pointerB:]:
            merged_arr[merge_pointer] = element
            merge_pointer += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # call recursively to split arr in half until all split arrays are <= len(1)
    #then take each pair of arrays as the recursion calls unwind and merge them in sorted order
    if len(arr) <= 1:
        return arr
    else:
        merge_sort(arr[:(len(arr) // 2)])
        merge_sort(arr[(len(arr) // 2):])


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass

def merge_sort_in_place(arr, l, r):
    pass


