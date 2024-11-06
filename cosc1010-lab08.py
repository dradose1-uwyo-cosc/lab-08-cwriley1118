# Colton Riley
# UWYO COSC 1010
# Submission Date 11/6/26
# Lab 08
# Lab Section: 15
# Sources, people worked with, help given to:
# Used https://www.w3schools.com/python/python_try_except.asp even though i have used try-except blocks before to make sure i know how it works


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
def is_number(arg):
    try:
        output = int(arg)
        return output
    except ValueError:
        try:
            output = float(arg)
            return output
        except ValueError:
            return False

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
yvalues = []
def main():
    while True:
        m = input("Enter your slope, m or 'exit' to quit: ")
        if is_number(m):
            m = is_number(m)
        elif 'exit' in m:
            break
        else:
            print("Please enter a usable value for m")

        b = input("Enter your y-intercept, b or 'exit' to quit: ")
        if is_number(b):
            b = is_number(b)
        elif 'exit' in b:
            break
        else:
            print("Please enter a usable value for b")
        
        lx = input("Enter your lower x bound or 'exit' to quit: ")
        if is_number(lx):
            lx = is_number(lx)
        elif 'exit' in lx:
            break
        else:
            print("Please enter a usable value for lx")

        ux = input("Enter your upper x bound or 'exit' to quit: ")
        if is_number(ux):
            ux = is_number(ux)
        elif 'exit' in ux:
            break
        else:
            print("Please enter a usable value for ux")

        if lx > ux:
            print("Please enter correct bounds")
        else:
            break
        
    for i in range(lx, ux):
        y = (m * i) + b
        yvalues.append(y)

main()
print(yvalues)
print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
