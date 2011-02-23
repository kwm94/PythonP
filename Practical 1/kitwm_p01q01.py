# filename:fahrenheit_to_celsius
# Name: Kit Wei Min
# Converts Fahrenheit to Celsius

# Prompt for the temperature in fahrenheit
fahrenheit = float(input("Temperature in fahrenheit:"))

# converts from fahrenheit to celsius
celsius = (5/9) * (fahrenheit - 32)

# print("Temp in Celsius = ", "{0:<30.2f}".format(celsius))

print ("{0:30s}{1:<4.2f}".format("Temperature in celsius = ", celsius))
