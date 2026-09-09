ch = input("enter one character ")

if ch.isupper():
    print(f"the given {ch} is uppercase")

elif ch.islower():
    print(f"the given {ch} is lowercase")


elif ch.isdigit():
    print(f"the number {ch} is a digit")

else:
    print(f"the given character {ch} is a special character")

