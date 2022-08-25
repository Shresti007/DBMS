# generic principle first choose pivot element mostly last element from array
# 2. After first call, stores element less than pivot in left sub array and elements great than pivot in right sub arr.
# 3. call quicksort recursively on left sub array.
#    then cal quick sort on right sub array.
def quicksort(arr, left, right):  # left aand right are indexes of arr we want ot sort
    if left < right:  # checking whether sub array consist atleast two elements
        # here we are choosing pivot from below function
        partition_pos = find_partition(arr, left, right)  # its a partition function calling it and declaring same arr
        # calling quicksort function recursively on left of pivot
        quicksort(arr, left, partition_pos - 1)  # we are calling quick sort on sub array after firs cal of partition
        # calling quick sort function recursively on ele next to pivot
        quicksort(arr,partition_pos+1, right)

def find_partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    while i < j:  # here i moves to right and j moves to left stops when both crossed each other
        while i < right and arr[i] < pivot:  # checking here if i is less than pivot it keeps on go and stop where
            # it is grtr than pivot
            i += 1  # increment if i less than pivot
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:  # just check as botht he elements are crossed at
            arr[i], arr[j] = arr[j], arr[i]  # if they didnt cross we need to swap both location of i and j element

    # if cross happens
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i


arr = [22, 11, 88, 66, 55, 77, 33, 44]
quicksort(arr, 0, len(arr) - 1)
print(arr)
