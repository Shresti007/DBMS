"""Binary Search: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval
covering the whole array. If the value of the search key is less than the item in the middle of the interval,
narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is
found or the interval is empty. """
# Compare x with the middle element. If x matches with the middle element, we return the mid index. Else If x is
# greater than the mid element, then x can only lie in the right half subarray after the mid element. So we recur for
# the right half. Else (x is smaller) recur for the left half.

def binarysearch(arr, n, target):
    left = 0
    right = n  # right = len(arr)-1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


# linear search
arr = [1, 2, 4, 5, 8, 10, 13, 14, 21, 29, 30, 31, 36, 39, 40, 43]
target = 80

print(binarysearch(arr, 10, 80))
print(binarysearch(arr, 10, 69))


# using for loop in linear search
def linearSearch(arr, n, targetvalue):
    for i in range(0, n):
        if arr[i] == target:
            return i
    return -1


arr = [7, 6, 3, 8, 9]
print(linearSearch(arr, 5, 3))
print(linearSearch(arr, 5, 9))


# Iterative binary Search Function method Python Implementation


# It returns index of n in given list1 if present,
# else returns -1
def binary_search(list1, n):
    low = 0
    high = len(list1) - 1
    mid = 0

    while low <= high:
        # for get integer result
        mid = (high + low) // 2

        # Check if n is present at mid
        if list1[mid] < n:
            low = mid + 1

            # If n is greater, compare to the right of mid
        elif list1[mid] > n:
            high = mid - 1

            # If n is smaller, compared to the left of mid
        else:
            return mid

            # element was not present in the list, return -1
    return -1


# Initial list1
list1 = [12, 24, 32, 39, 45, 50, 54]
n = 45

# Function call
result = binary_search(list1, n)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in list1")
