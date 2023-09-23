# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height != 120:
#     print("You can go")
# else:
#     print("You can not go bro")

number = int(input("Which number do you want to check? "))
number %= 2
if number == 1:
    print("This is an odd number.")
else:
    print("This is an even number.")