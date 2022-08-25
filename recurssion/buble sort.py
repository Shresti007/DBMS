# COMPARISION BASED ALGORITHM
# Programing with Mosh
# bubble sort is sorted in ascending order, comparing from left of two adjacent elements, if right one is smaller than
# LEFT, SWAPing is happened. so in each pass right most index is settled with higher element. n in first pass, n-1
# in second pass

"""Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are
in wrong order.
xample:
 First Pass:
( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.
Second Pass:
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )

 Now, the array is already sorted, but our algorithm does not know if it
is completed. The algorithm needs one whole pass without any swap to know it is sorted. Third Pass:
( 1 2 4 5 8 ) –>( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) """


def bubble_sort(arr, n):
    for i in range(0, n - 1):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:  # left ele is greater than right then swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


arr = [56, 8, 12, 89, 10]
bubble_sort(arr, 5)
print(arr)
