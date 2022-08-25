"""
Postfix: An expression is called the postfix expression if the operator appears in the expression after the operands.
Simply of the form (operand1 operand2 operator).
Example : AB+CD-* (Infix : (A+B) * (C-D) )

Prefix : An expression is called the prefix expression if the operator appears in the expression before the operands.
Simply of the form (operator operand1 operand2).
Example : *+AB-CD (Infix : (A+B) * (C-D) )
Given a Postfix expression, convert it into a Prefix expression.
Conversion of Postfix expression directly to Prefix without going through the process of converting them first to Infix
and then to Prefix is much better in terms of computation and better understanding the expression (Computers evaluate
using Postfix expression).

Algorithm for Postfix to Prefix:


Read the Postfix expression from left to right
If the symbol is an operand, then push it onto the Stack
If the symbol is an operator, then pop two operands from the Stack
Create a string by concatenating the two operands and the operator before them.
string = operator + operand2 + operand1
And push the resultant string back to Stack
Repeat the above steps until end of Prefix expression.
"""


# Python3 Program to convert postfix to prefix

# function to check if
# character is operator or not


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


# Convert postfix to Prefix expression


def postToPre(post_exp):
    s = []

    # length of expression
    length = len(post_exp)

    # reading from right to left
    for i in range(length):

        # check if symbol is operator
        if (isOperator(post_exp[i])):

            # pop two operands from stack
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()

            # concat the operands and operator
            temp = post_exp[i] + op2 + op1

            # Push string temp back to stack
            s.append(temp)

        # if symbol is an operand
        else:

            # push the operand to the stack
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





