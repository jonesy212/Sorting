# TO-DO: Complete the selection_sort() function below 

def selection_sort(arr):

def selection_sort(arr):
    for i in range(0, len(arr)-1):
        cur__index = i
        smallest_index = cur_index
        #find the next smallest element q
        for x in range(cur_index, len(arr)):
            if arr[x] < arr[smallest_index]:
                #found new smallest thing!
                smalles_index = x
    # loop through everything but the last element

    return arr

# Always pick first element as pivot.
# Always pick last element as pivot (implemented below)
# Pick a random element as pivot.
# Pick median as pivot.


            # *compare first and last number
            # *if second number is bigger than the 
            #     one to the left,  swap


# # TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swap = True
    while swap:
        swap = False
        for i range(0, len(arr)-1):
            current_index = i
            next_index = i + 1
            if arr[i] > arr[next_index]:
                arr[i], arr[next_index] = arr[next_index], arr[i]
                swap = True
    return arr
# print(arr.sort())


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr

