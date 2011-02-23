# File name: even_or_odd.py
# Name: Kit Wei Min
# Description: Checks if the integer inputed is even or odd

# Prompts user for an integer
num = int(input("Enter an integer: "))

# Checks if the number is even or odd and displays the result.

if num % 2 == 0:
    print("{0} is an even number".format(num))
else:
    print("{0} is an odd number".format(num))
