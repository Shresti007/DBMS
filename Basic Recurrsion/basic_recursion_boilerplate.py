def Fibonacci(n):
    """Implement the method below to calculate the nth fibonacci value."""
    if n < 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


if __name__ == '__main__':
    nth_fibonacci = int(input())
    print("Fibonacci value at position " + str(nth_fibonacci) + " is " + str(Fibonacci(nth_fibonacci)))
