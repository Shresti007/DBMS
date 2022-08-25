# comparison based algorithm along with bubble sort , selection sort
# outer loop iterate from arr[1] to arr[n]
# compare the element to its predecessor, if element < predecessor= move the element to the right keep checking this

"""Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands.
The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed
at the correct position in the sorted part. Algorithm To sort an array of size n in ascending order: 1: Iterate from
arr[1] to arr[n] over the array. 2: Compare the current element (key) to its predecessor. 3: If the key element is
smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make
space for the swapped element. """
# 12, 11, 13, 5, 6
# Let us loop for i = 1 (second element of the array) to 4 (last element of the array)
# i = 1. Since 11 is smaller than 12, move 12 and insert 11 before 12
# 11, 12, 13, 5, 6
# i = 2. 13 will remain at its position as all elements in A[0..I-1] are smaller than 13
# 11, 12, 13, 5, 6
# i = 3. 5 will move to the beginning and all other elements from 11 to 13 will move one position ahead of their
# current position.
# 5, 11, 12, 13, 6
# i = 4. 6 will move to position after 5, and elements from 11 to 13 will move one position ahead of their current
# position.
# 5, 6, 11, 12, 13


def insertion_sort(arr, n):  # FelixTechTips

    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:  # here checking left neighbour arr( j-1) is greater than arr(j) and we
            # dont want j to be zero so condition is j>0. because we taken left most index is sorted as condition in
            # insertion sort.
            arr[j - 1], arr[j] = arr[j], arr[j - 1]  # if so it is great swap elements botha done in this line
            j -= 1  # here it states we have to move left and compare so check s done in this way


arr = [56, 8, 12, 89, 10]
insertion_sort(arr, 5)
print(arr)
