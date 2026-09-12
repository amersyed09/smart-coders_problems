n = int(input("enter the number"))
k = int(input("enter one more number:"))

if n & (1 << k):
    print(" it is a Set")
else:
    print("it is Not a Set")
