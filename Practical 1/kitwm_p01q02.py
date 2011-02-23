# File name:vol_of_cylinder
# Author: Kit Wei Min
# Description: computing volume of cylinder

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
