# task 1

number1, number2, number3 = input("Enter the first number: "), input("Enter the second number: "), input("Enter the third number: ")

if number2 < number3 < number1:
    print("number 1 is biggest and number 2 is smallest")
elif number2 < number1 < number3:
    print("number 3 is biggest and number 2 is smallest")
elif number1 < number2 < number3:
    print("number 3 is biggest and number 1 is smallest")
elif number1 < number3 < number2:
    print("number 2 is biggest and number 1 is smallest")
elif number3 < number1 < number2:
    print("number 2 is biggest and number 3 is smallest")
elif number3 < number2 < number1:
    print("number 1 is biggest and number 3 is smallest")
else:
    print("some of your numbers are equal")

# in this code the numbers are input by user
# then checks for size difference
# it compares to find both the smallest and the largest

