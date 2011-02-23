# Filename: fahrenheit_to_celsius
# Name: Kit Wei Min
# Description: Converts temperature from Fahrenheit to Celsius

# Prompt for the temperature in fahrenheit
fahrenheit = float(input("Temperature in fahrenheit: "))

# Converts from fahrenheit to celsius
celsius = (5/9) * (fahrenheit - 32)

# workable: print("Temp in Celsius = ", "{0:<30.2f}".format(celsius))

print ("{0:25s}{1:<4.2f}".format("Temperature in celsius = ", celsius))
