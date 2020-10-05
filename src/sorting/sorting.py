# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):

    arrC = []
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] > arrB[0]:
            arrC.append(arrB.pop(0))
        else:
            arrC.append(arrA.pop(0))
    while len(arrA) > 0:
        arrC.append(arrA.pop(0))
    while len(arrB) > 0:
        arrC.append(arrB.pop(0))
    return arrC


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # call recursively to split arr in half until all split arrays are <= len(1)
    #then take each pair of arrays as the recursion calls unwind and merge them in sorted order
    #pseudocode
    if len(arr) <= 1:
        return arr
    arr1 = [x for x in arr[:len(arr)//2]]
    arr2 = [x for x in arr[len(arr)//2:]]

    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)

    return merge(arr1, arr2)



# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass

def merge_sort_in_place(arr, l, r):
    pass


