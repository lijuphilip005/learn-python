 
age = int(input("please enter your age"))

price=10


if age > 70:
    print(f"you have extra charges,{price*0.75} ,please pay and continue")
elif age > 18:
    print("your are an adult ,please take a ticket for entry")
else:
    print("you may enter no need to take ticket")    