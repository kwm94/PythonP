# File Name: determining_leap_year.py
# Name: Kit Wei Min
# Description: Determines if the year entered by the user is a leap year.


# Prompts user to enter a year
year = int(input("Enter a year: "))

# Determines if the year is a leap year and displays the result.

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print ("Leap year")
else:
    print ("Non leap year")
