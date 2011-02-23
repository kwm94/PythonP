# File name: Summing_digits_in_integer
# Name: Kit Wei Min
# Sums up the digits in an integer


# Prompt for integer
integer = int(input("Enter an integer between 0 and 1000: "))

# Add up the sum of the digits =D
sum = (integer % 10) + ((integer // 10) % 10) + (integer // 100)

# Display the sum
print ("Sum of the digits = {0:2}".format(sum))


# extract digits
# x = num % 10
# num = num // 10
# y = num % 10
# num = num // 10
# z = num % 10
# num = num // 10

# sum = x + y + z

# hint : 932 % 10 = 2 and 932 // 10 = 93
