# File name: vol_of_cylinder
# Name: Kit Wei Min
# Description: computing the volume of a cylinder, given its radius and length

import math

# Prompt for radius of cylinder
radius = float(input("Radius = "))

# Prompt for length of cylinder
length = float(input("Length = "))

# Computes volume of cylinder
area = radius * radius * math.pi
volume = area * length

# Displays the volume
print("Volume = {0:2.2f}".format(volume))
