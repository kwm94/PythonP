# File Name: days_in_month.py
# Name: Kit Wei Min
# Description: Displays the number of days in the month of a year entered by the user.


# Prompts user to input the month and year.
yr = int(input("Enter a year: "))
mth = int(input("Enter the month: "))

# Determines the number of days in the month of the year entered and displays the result.

if mth == 1:
    print("January " + str(yr) + " has 31 days.")

elif mth == 2:
    if yr % 4 == 0 and yr % 100 != 0 or yr % 400 == 0:
        print("February " + str(yr) + " has 29 days.")
    else:
        print("February " + str(yr) + " has 28 days.")
        
elif mth == 3:
    print("March " + str(yr) + " has 31 days.")

elif mth == 4:
    print("April" + str(yr) + "has 30 days.")
    
elif mth == 5:
    print("May " + str(yr) + " has 31 days.")

elif mth == 6:
    print("June " + str(yr) + "has 30 days.")
    
elif mth == 7:
    print("July" , yr , "has 31 days.")

elif mth == 8:
    print("August" , yr , "has 31 days.")

elif mth == 9:
    print("September" , yr , "has 30 days.")
    
elif mth == 10:
    print("October" , yr , "has 31 days.")

elif mth == 11:
    print("November" , yr , "has 30 days.")
              
elif mth == 12:
    print("December" , yr , "has 31 days.")
