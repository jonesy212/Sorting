# TO-DO: complete the help function below to merge 2 sorted arrays
# def merge( arrA, arrB ):
#     elements = len( arrA ) + len( arrB )
#     merged_arr = [0] * elements
#     # TO-DO
#     merge =[]
#     for i in range(0, elements):
#         if arrA[0] < arrB[0]:
#             merged_arr[i] = arrA[i]
#             merged_arr[i + len(arrA)] = arrB[i]
        
#         if arrA[0] > arrB[0]:
#            merged_arr[i] = arrB[i]
#            merged_arr[i + len(arrB)] = arrA[i]
#         print(merged_arr)

#     return merged_arr

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    print(elements / 2)
    for i in range(0, int(elements) // 2 ):
        if arrA[0] < arrB[0]:
            merged_arr[i] = arrA[i]
            print(merged_arr)
        if arrA[0] > arrB[0]:
           merged_arr[i] = arrA[i+len(arrB)]
    for i in range(0, int(elements) // 2 ):
        if arrA[0] < arrB[0]:
            merged_arr[i+len(arrA)] = arrB[i]
        if arrA[0] > arrB[0]:
            merged_arr[i] = arrB[i]
    print(merged_arr)
    # print(merged_arr)
    return merged_arr
merge([0,1,2,3,4],[5,6,7,8,9])


def merge( arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] + elements

    for i in range(merged_arr):
    #1. LHS is empty
        #copy RHS to merged_arr
    #2. RHS is empty
        #copy LHS to merged_arr
    #3. front of LHS < front of RHS
        merged_arr[i] = arrA[0]
        arrA.pop(0)
    #4. front of the right hand side of the LHS  (3) 6   (2)45
        merged.arr[i] = arrB[0]
        arrB.pop(0)

def merge_sort(arr):
    #break list in half until len(list) == 1
    if len(arr < 1):
        lhs = merge_sort(arr[:len(arr)//2])
        rhs = merge_sore(arr[len(arr)//2:])
        merge(lhs,rhs)

    return arr
#//  must be used  to do index iteration
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    #break list in half until len(list) == 1
    if len(arr < 1):
        lhs = merge_sort(arr[:len(arr)//2])
        rhs = merge_sort(arr[len(arr)//2:])
        merge(lhs,rhs)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    if len(arr < 1):
        start = merge_in_place(arr)
        merge(start, mid, end)

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
