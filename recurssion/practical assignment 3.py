def linearsearch(arr,n, target):
    for i in range(0,n):
        if arr[i]== target:
            return i
    return -1

arr = [1,2,3,4,5,6,8]
print(linearsearch(arr,len(arr),3))
print(linearsearch(arr,len(arr),10))
