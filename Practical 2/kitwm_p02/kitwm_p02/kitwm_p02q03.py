# File Name: determining_grade.py
# Name: Kit Wei Min
# Description: Determines the grade of the score (0 to 100) entered.

# Promts user to enter a score
score = int(input("Enter a score (bwt 0 and 100 incl): "))

# Determines the grade and displays it

if score >= 70:
    print ("Grade: A")
elif 60 <= score < 70:
    print ("Grade: B")
elif 55 <= score < 60:
    print ("Grade: C")
elif 50 <= score < 55:
    print ("Grade: D")
elif 45 <= score < 50:
    print ("Grade: E")
elif 35 <= score < 45:
    print ("Grade: S")
else:
    print ("Grade: U")
