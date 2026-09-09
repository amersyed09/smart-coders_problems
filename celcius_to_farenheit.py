a = int(input("SELECT\n 1.to convert celcius to farenheit \n 2. to convert faremheit to celcius :"))
if a == 1:
    c = float(input("enter celcius value:"))
    b=c *(9/5) + 32
    print("farenheit value is :", b)

elif a==2  :
    f = float(input("enter farenheit value :"))
    c=(f-32)*(5/9)
    print("celcius value is :", c)