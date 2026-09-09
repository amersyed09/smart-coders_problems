n = int(input("enter a number :"))
if n %3 ==0 and n%5 ==0:
    print(f"the given number {n} is divisible by 3 and 5")

elif n %3 ==0 :
    print(f"the given number {n} is divisible by 3")


elif n %5 ==0 :
    print(f"the given number {n} is divisible by 5")

else :
    print(f"the given number {n} is not divisible by both 3 and 5")

