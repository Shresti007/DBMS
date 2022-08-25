# The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
# from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
# 1) The subarray which is already sorted.
# 2) Remaining subarray which is unsorted.
# In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray
# is picked and moved to the sorted subarray.
# Following example explains the above steps:

def selection(arr, n):
    for i in range(n):        # here i is recognsied as
        least = i             #     here we have taken initially min val as i i.e: where ever i starts we take it for
                              # just at that time as min val unitll we find is there any min val
        for j in range (i+1, n):       # here while i satys, j will iterate from i+1 to n in search of lowest value
            if(arr[least])>arr[j]:      # here we are checking if there is any value less than least .
                least =j                # so if u found any value less than least, then j is to be swapped with least
        arr[i], arr[least] = arr[least], arr[i]
    return arr;

arr = [56,8,12,89,10]
selection(arr,5)
print(arr)