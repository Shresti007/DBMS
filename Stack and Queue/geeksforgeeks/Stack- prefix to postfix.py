""""
Prefix: An expression is called the prefix expression if the operator appears in the expression before the operands.
Simply of the form (operator operand1 operand2).
Example : *+AB-CD (Infix : (A+B) * (C-D) )

Postfix: An expression is called the postfix expression if the operator appears in the expression after the operands.
Simply of the form (operand1 operand2 operator).
Example : AB+CD-* (Infix : (A+B * (C-D) )
Given a Prefix expression, convert it into a Postfix expression.
Conversion of Prefix expression directly to Postfix without going through the process of converting them first to Infix
 and then to Postfix is much better in terms of computation and better understanding the expression (Computers evaluate
 using Postfix expression).


Algorithm for Prefix to Postfix:

Read the Prefix expression in reverse order (from right to left)
If the symbol is an operand, then push it onto the Stack
If the symbol is an operator, then pop two operands from the Stack
Create a string by concatenating the two operands and the operator after them.
string = operand1 + operand2 + operator
And push the resultant string back to Stack
Repeat the above steps until end of Prefix expression.
"""
# https://youtu.be/MeRb_1bddWg

# Write Python3 code here
# -*- coding: utf-8 -*-

# Example Input
s = "*-A/BC-/AKL"    # if conveted to infix it is like --> (A-(B/C)*(A/K)-L) TO POST FIX -> ABC/-AK/L-*

# Stack for storing operands
stack = []
operators = set(['+', '-', '*', '/', '^'])

# Reversing the order
s = s[::-1]

# iterating through individual tokens
for i in s:

    # if token is operator
    if i in operators:

        # pop 2 elements from stack
        a = stack.pop()
        b = stack.pop()

        # concatenate them as operand1 +
        # operand2 + operator
        temp = a + b + i
        stack.append(temp)

    # else if operand
    else:
        stack.append(i)

# printing final output
print(*stack)
