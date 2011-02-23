# File Name: sorts_integers.py
# Name: Kit Wei Min
# Description: Program sorts the three integers entered and displays it in decreasing order after sorting.


# Prompts user to enter three integers

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))


numbers = [num1, num2, num3]

if num1 > num2 > num3:
    print(numbers[0], numbers[1], numbers[2])
elif num1 > num3 > num2:
    print(numbers[0], numbers[2], numbers[1])
elif num2 > num1 > num3:
    print(numbers[1], numbers[0], numbers[2])
elif num2 > num3 > num1:
    print(numbers[1], numbers[2], numbers[0])
elif num3 > num1 > num2:
    print(numbers[2], numbers[0], numbers[1])
elif num3 > num2 > num1:
    print(numbers[2], numbers[1], numbers[0])
