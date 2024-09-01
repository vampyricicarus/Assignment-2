# task 1

numberInput = input("Pick a year: ")
number = int(numberInput)

if number % 100 == 0:
    leapYear = number % 400 == 0
else:
    leapYear = number % 4 == 0

if leapYear == True:
    print("True")
else:
    print("False")

# these two if statements break up the question into two manageable parts