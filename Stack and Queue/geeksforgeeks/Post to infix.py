"""Infix expression: The expression of the form a op b. When an operator is in-between every pair of operands.
Postfix expression: The expression of the form a b op. When an operator is followed for every pair of operands.
Postfix notation, also known as reverse Polish notation, is a syntax for mathematical expressions in which the
mathematical operator is always placed after the operands. Though postfix expressions are easily and efficiently
evalua ted by computers, they can be difficult for humans to read. Complex expressions using standard parenthesized
infix notation are often more readable than the corresponding postfix expressions. Consequently, we would sometimes
like to allow end users to work with infix notation and then convert it to postfix notation for computer processing.
Sometimes, moreover, expressions are stored or generated in postfix, and we would like to convert them to infix for
the purpose of reading and editing

 Algorithm
1.While there are input symbol left
…1.1 Read the next symbol from the input.
2.If the symbol is an operand
…2.1 Push it onto the stack.
3.Otherwise,
…3.1 the symbol is an operator.
…3.2 Pop the top 2 values from the stack.
…3.3 Put the operator, with the values as arguments and form a string.
…3.4 Push the resulted string back to stack.
4.If there is only one value in the stack
…4.1 That value in the stack is the desired infix string.

Below is the implementation of above approach:

 """


# Python3 program to find infix for
# a given postfix.
def isOperand(x):
    return (('a' <= x <= 'z') or
            ('A' <= x <= 'Z'))


# Get Infix for a given postfix
# expression
def getInfix(exp):
    s = []

    for i in exp:

        # Push operands
        if (isOperand(i)):
            s.insert(0, i)

        # We assume that input is a
        # valid postfix and expect
        # an operator.
        else:

            op1 = s[0]
            s.pop(0)
            op2 = s[0]
            s.pop(0)
            s.insert(0, "(" + op2 + i + op1 + ")")

    # There must be a single element in
    # stack now which is the required
    # infix.
    return s[0]


# Driver Code
if __name__ == '__main__':
    exp = "ab*c+"
    print(getInfix(exp.strip()))

# This code is contributed by
# Shubham Singh(SHUBHAMSINGH10)
