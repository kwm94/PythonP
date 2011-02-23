# Filename : ASCII_character
# Name : Kit Wei Min
# Description : Displays the character of an ASCII code.


# Prompts for an ASCII code

code = int(input("Enter ASCII code (between 0-127 exclusive): "))

# Converts ASCII code

character = chr(code)

print("Character of code: " "{0}". format(character))
