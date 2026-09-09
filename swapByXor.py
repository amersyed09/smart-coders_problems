a = int(input("Enter a number:"))
b= int(input("Enter another number :"))

print(f"old a {a}")
print(f"old b {b}")
a = a^b
b = a^b
a = a^b

print("current a is ", a)
print("current b is ", b)