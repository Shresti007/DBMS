def isDuplicateLinear(arr):
    for i in range(0, len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

def isDuplicateBinary(arr):
    arr.sort()
    for i in range(0, len(arr)):
        if binarySearch(arr, i+1, len(arr)-1, arr[i]):
            return True
    return False


def binarySearch(arr,left,right,target):
    if left>right:
        return False
    mid=left+(right-left)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return binarySearch(arr,left,mid-1, target)
    else:
        return binarySearch(arr,mid+1,right,target)


arr = [1,2,7,5,8,9]
print(isDuplicateLinear(arr))
print(isDuplicateBinary(arr))