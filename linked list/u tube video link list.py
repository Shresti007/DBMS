def Multiplication(num1,num2):
    if num1<num2:
        return Multiplication(num2, num1)
    elif num2!=0:
        return num1 + Multiplication(num1, num2 - 1)
    else:
        return 0
print("Enter the two Number:")
num1=int(input())
num2=int(input())
print("Multiplication of Two Number Using Recursion is: ",Multiplication(num1,num2))