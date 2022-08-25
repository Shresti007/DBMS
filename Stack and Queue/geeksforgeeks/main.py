def isOperator(x):
    if x == "+":
        return True

    if x == "-":
        return True

    if x == "/":
        return True

    if x == "*":
        return True

    return False


def postToPre(post_exp):

    s = []

    length = len(post_exp)
    for i in range(length):
        if isOperator(post_exp[i]):
            # pop the two elements from stack top two
            a = s[-1]
            s.pop()
            b = s[-1]
            s.pop()
            temp = post_exp[i] +b + a
            s.append(temp)
        else:
            s.append(post_exp[i])
    ans = ""
    for i in s:
        ans += i
    return ans


# Driver Code
if __name__ == "__main__":
    post_exp = "AB+CD-"

    # Function call
    print("Prefix : ", postToPre(post_exp))

# This code is contributed by AnkitRai01

