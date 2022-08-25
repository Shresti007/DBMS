def MaxTimesElement(arr):
    MaxRepeatingelement= arr[0]
    MaxCount= 1
    for i in range(0, len(arr)):
        count= 1
        for j in range(i+1, len(arr)):
            if arr[i]==arr[j]:
                count+=1
            if count>MaxCount:
                maxCount=count
                MaxRepeatingele= arr[i]
    return MaxRepeatingele

arr =[1,3,2,1,4,1,3,2,3,8,3]
print(MaxTimesElement(arr))