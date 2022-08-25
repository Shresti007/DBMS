# how many times element has been presented in input it counts element frequency and then sorts the algo.
# first step --> create an auxiliary array
# second step --> modify the count array, each index element contains sum of all previous index elements.
# sum mean indicates the position of each object in the output reference.
# Iterate through the input array --> try to find the value in the count array


def countsort(arr, max_value):
    count = [0]*(max_value+1)    # here new auxilary array will have k+1 el, ie is max valu+1
    for item in arr:
        count[item]+=1
    num_item_before = 0

    for i, count in enumerate(count):
        count[i] = num_item_before
        num_item_before += count

    sorted_list = [none]*len(arr)

    for item in arr:
        sorted_list[count[item]]=item
        count[item] += 1

    return sorted_list


arr = [56,812,89,10]
max_ele = max(arr)
sorted_arr = countsort(arr, max_ele)
print(sorted_arr)