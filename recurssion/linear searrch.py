    # using iterative method
pos = -1       # global variable when list is empty
def search(list, n):
    i = 0
    while i <len(list): # it is list so index value starts from 0 so we are not taking i<=len(list
        if list[i] == n:
            globals()['pos'] = i      # local variable i using to find its index position in linear search
            return True
        i = i+1
    return False


list = [5,8,4,6,9,2,30,40,50,60,70]
n = 50
if search(list,n):
    print("found at", pos+1)
else:
    print("not found")


