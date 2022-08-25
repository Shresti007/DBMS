# n!/(k!⋅(n−k)!)

def n_choose_k(n, k):

    return recursive_factorial(n) / (iterative_factorial(k) * recursive_factorial(n - k))


def recursive_factorial(num):
    """Implement the recursive method to return the factorial of a number."""
    if num == 1:
        return 1
    else:
        return (num * recursive_factorial(num - 1))

def iterative_factorial(num):
    """Implement an iterative method to return the factorial of a number."""
    if num < 0:
        return 0
    elif num == 0 or num == 1:
        return 1
    else:
        fact = 1
        while (num > 1):
            fact *= num
            num -= 1
        return fact



if __name__ == '__main__':
    print("Total possible combinations of hands to be dealt: " + str(n_choose_k(52, 2)))
    print("Total possible combinations of 5 cards, to be put down as Flop + Turn + River: " + str(n_choose_k(52, 5)))


