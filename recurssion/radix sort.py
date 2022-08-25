def __get_num_digits(A):   # get number of digits in largest item
    m = 0
    for item in A:
        m = max(item, m)
    return len(str(m))

def radix(A, num_digits):
    for digit in range(0, num_digits):
        B = [[] for i in range (10)]

def main():
    A = [55,45,3,289,213,1,288,53,2]
    num_digits = __get_num_digits(A)
    A = radix(a, num_digits)
    print(A)

main()