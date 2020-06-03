# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # loop through the array again this time start the loop 1 ahead of i - this will check everything on the right of
        # the current index
        for j in range(i + 1, len(arr)):
            # compare the array at position j with whatever is the current smallest item in the array
            # if array at position j is smaller than we can update the smallest index
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # Store the items i want to swap in variables
        current = arr[cur_index]
        smallest = arr[smallest_index]
        # and then swap them out with eachother
        arr[smallest_index] = current
        arr[cur_index] = smallest

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr