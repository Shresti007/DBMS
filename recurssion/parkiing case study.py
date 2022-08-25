from datetime import datetime

def binary_search(arr,x):
    l = 0
    r = len(arr)-1
    mid = 0
    x = datetime.strptime(x, "%Y/%m/%d")

    while l <= r:

        mid = l+(r-l)//2

        mid_date = datetime.strptime(arr[mid], "%Y/%m/%d")

        if mid_date == 0:
            return mid
        elif mid_date > x:
            r = mid-1
        else:
            l = mid+1

    return -1

if __name__ =='__main__':
    Parking_History = ["2020/09/01", "2020/09/02", "2020/09/03", "2020/09/04", "2020/09/05", "2020/09/08", "2020/09/10", "2020/09/15"]

    print("Please mention the date to be queried, format 'YYYY/MM/DD'")
    search_date = str(input())

    #Fucntion call
    result = binary_search(Parking_History, search_date)
    if result:
        print("vehicle was parked at queried date:" + str(search_date))
    else:
        print("Vehicle was not parked at queried date")
