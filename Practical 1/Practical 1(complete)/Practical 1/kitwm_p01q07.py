# Filename : Payroll
# Name : Kit Wei Min
# Description : prints a payroll statement

# Prompts user for the information
name = input("Enter name : ")
wkhrs = int(input("Enter number of hours worked weekly : "))
payr = float(input("Enter hourly pay rate : "))
cpfr = float(input("Enter CPF contribution rate(%) : "))


# Calculates the values in the payroll statement
gpay = wkhrs * payr
cpfc = cpfr / 100 * gpay
npay = gpay - cpfc



# Displays the payroll statement

print("")
print("Payroll statement for {0:20s}".format(name))
print("Number of hours worked in week : {0}".format(wkhrs))
print("Hourly pay rate                : ${0:<10.2f}".format(payr))
print("Gross pay                      : ${0:<10.2f}".format(gpay))

print("CPF contribution at {0:2.0f}%        : ${1:<10.2f}".format(cpfr, cpfc))
print("Net pay                        : ${0:<10.2f}".format(npay))


## Comments:
## we should use meaningful variable names. and put the date started at the top.
## Even though its not stated, should try to align the output.
## (aligning the output can be done with the {0:32} etc etc. 
## print() will aso print a blank line.
