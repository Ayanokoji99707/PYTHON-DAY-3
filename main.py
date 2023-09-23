print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height != 120:
    print("You can go")
else:
    print("You can not go bro")

x = int(input("What Number do you want to check ?"))
x %= 2
if x == 1:
    print("This is oda number")
else:
    print("This is even number")

height = int(input("What is your Height? "))

if height >= 120:
    print("Go TO Railway")
    age = int(input("what is your age? "))
    if age >= 18:
        print("Your Ticket Price is $12")
    elif age >= 12:
        print("your Ticket is $7")
    elif age < 12:
        print("Your Ticket price is $5")
    else:
        print("You can not go to railway")
else:
    print("Sorry, you should not go")
