# A Python 3 program to
# demonstrate working of
# recursion


def printFun(test):
    if (test < 1):
        return
    else:

        print(test, end=" ")
        printFun(test - 1)  # statement 2
        print(test, end=" ")
        return


# Driver Code
test = 3
printFun(test)


# This code is contributed by
# Smitha Dinesh Semwal


# Python code to implement Fibonacci series base case stop at n = 2

# Function for fibonacci
def fib(n):
    # Stop condition
    if (n == 0):
        return 0

    # Stop condition
    if (n == 1 or n == 2):
        return 1

    # Recursion function
    else:
        return (fib(n - 1) + fib(n - 2))


# Driver Code

# Initialize variable n.
n = 5;
print("Fibonacci series of 5 numbers is :", end=" ")

# for loop to print the fiboancci series.
for i in range(0, n):
    print(fib(i), end=" ")


# Python3 code to implement factorial

# Factorial function
def f(n):
    # Stop condition
    if n == 0 or n == 1:
        return 1

    # Recursive condition
    else:
        return n * f(n - 1)


# Driver code
if __name__ == '__main__':
    n = 5
    print("factorial of", n, "is:", f(n))

# This code is contributed by pratham76.
