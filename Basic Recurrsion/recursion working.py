# sum of naturals using recurssion
def add_naturals(x):
    if x==1:
        return 1
    return (x + add_naturals(x-1))

n = int(input("enter a num: "))
sum = add_naturals(n)
print("sum is:", sum)

# problem to convert int using recursive approach
def to_string(n,base):
   conver_tString = "0123456789ABCDEF"
   if n < base:
      return conver_tString[n]
   else:
      return to_string(n//base,base) + conver_tString[n % base]

print(to_string(2835,16))


def to_string(n,base):
   conver_tString = "0123456789ABCDEF"
   if n < base:
      return conver_tString[n]
   else:
      return to_string(n//base,base) + conver_tString[n % base]

print(to_string(2835,16))
