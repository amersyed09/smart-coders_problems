time = int(input("Enter time (in 24hrs zone):"))

if time < 12:
    print("Good Morning")
elif time < 17:
    print("Good Afternoon")
elif time < 21:
    print("Good Evening")
else:
    print("Good Night")