def merge_sort(arr,left, right):
    if len(arr) > 1:    # if arr is more than 1 element it is useful for merge sort
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

    #recursion
    merge_sort(left_arr)
    merge_sort(right_arr)

    #merge
    i = 0   # left arr indx
    j = 0   # right arr idx
    k = 0   #new arr idx
    while i < len(left_arr) and  j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = left_arr[i]
        j += 1
        k += 1


arr_test = [2,3,5,1,7,4,4,4,2,6,0]
merge_sort(arr_test)
print(arr_test)

def merge_sort(arr, left, right):

    if left<right:
        mid_indx= (left+(right-1))//2
        merge_sort(arr,left,mid_indx)
        merge_sort(arr,mid_indx+1, right)
        merge(arr, left, mid_indx, right)


def merge(arr, left, mid_indx, right):
    n1=mid_indx-left+1
    n2=right-mid_indx

    left_arr=[0]*n1
    right_arr=[0]*(n2)

    for i in range(0,n1):
        left_arr[i]=arr[left+i]
    for j in range(0,n2):
        right_arr[j]=arr[mid_indx+1+j]

    i=0
    j=0
    k = left

    while i<n1 and j<n2:
        if left_arr[i]<=right_arr[j]:
            arr[k]=left_arr[i]
            i+=1
        else:
            arr[k]=right_arr[j]
            j+=1
        k+=1
    while i<n1:
        arr[k]=left_arr[i]
        i += 1
        k += 1

    while j <= n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1


arr =[56,8,12,89,10]
merge_sort(arr,0,5)
print(arr, )


