# File name: validating_triangles_and_computing_perimeter.py
# Name: Kit Wei Min
# Description: Reads three edges of a triangle and determines if it is valid.
#              Valid if the sum of any two edges is greater than the third edge.
#              If input is valid, perimeter of the triangle will be computed and displayed.


# Prompts user for the three edges of a triangle

n1 = float(input("Enter the length of one edge of a triangle: "))
n2 = float(input("Enter the length of the second edge: "))
n3 = float(input("Enter the length of the third edge: "))

# determines if the input is valid and displays perimeter if input is valid.

peri = n1 + n2 + n3

if n1 + n2 <= n3 or n1 + n3 <= n2 or n2 + n3 <= n1 :
    print ("Invalid triangle!")
else:
    print ("Perimeter of triangle = {0:2.0f}".format(peri))
    
