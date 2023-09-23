height = int(input("What is your Height? "))

if height >= 120:
    print("Go TO Railway")
    age = int(input("what is your age? "))
    if age >= 18:
        print("Your Ticket Price is $12")
    elif age >= 12:
        print("your Ticket is $10")
    elif age >= 7:
        print("Your Ticket price is $7")
    else:
        print("You can not go to railway")
else:
    print("Sorry, you should not go")
