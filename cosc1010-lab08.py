# Colton Riley
# UWYO COSC 1010
# Submission Date 11/6/26
# Lab 08
# Lab Section: 15
# Sources, people worked with, help given to:
# Used https://www.w3schools.com/python/python_try_except.asp even though i have used try-except blocks before to make sure i know how it works
# Recieved help from Jedadia (appologies if that is spelled wrong) on the first part and i was using type error instead of valueerror
# Gave help to Colter on how i did the entireity of part two

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
            m1 = is_number(m)
        elif 'exit' in m.lower():
            break
        else:
            print("Please enter a valid value for m")
            continue

        b = input("Enter your y-intercept, b or 'exit' to quit: ")
        if is_number(b):
            b1 = is_number(b)
        elif 'exit' in b.lower():
            break
        else:
            print("Please enter a valid value for b")
            continue

        lx = input("Enter your lower x bound or 'exit' to quit: ")
        if is_number(lx):
            lx1 = is_number(lx)
        elif 'exit' in lx.lower():
            break
        else:
            print("Please enter a valid value for lx")
            continue

        ux = input("Enter your upper x bound or 'exit' to quit: ")
        if is_number(ux):
            ux1 = is_number(ux)
        elif 'exit' in ux.lower():
            break
        else:
            print("Please enter a valid value for ux")
            continue

        if lx1 > ux1:
            print("Please enter valid bounds")
            continue
        else:
            break
        
    for i in range(lx1, ux1 + 1):
        y = (m1 * i) + b1
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

# Use same as part two but with the three variables. For two answers do +sqrt and -sqrt. for sqrt do **. Also check that you cant devide by zero.

def main():
    while True:
        a = input("Enter your value for a (ax^2 + bx + c = 0) or 'exit' to quit: ")
        if is_number(a):
            a1 = is_number(a)
        elif 'exit' in a.lower():
            break
        else:
            print("Please enter a valid value for m")
            continue

        b = input("Enter your  or 'exit' to quit: ")
        if is_number(b):
            b1 = is_number(b)
        elif 'exit' in b.lower():
            break
        else:
            print("Please enter a valid value for b")
            continue

        lx = input("Enter your lower x bound or 'exit' to quit: ")
        if is_number(lx):
            lx1 = is_number(lx)
        elif 'exit' in lx.lower():
            break
        else:
            print("Please enter a valid value for lx")
            continue

        ux = input("Enter your upper x bound or 'exit' to quit: ")
        if is_number(ux):
            ux1 = is_number(ux)
        elif 'exit' in ux.lower():
            break
        else:
            print("Please enter a valid value for ux")
            continue

        if lx1 > ux1:
            print("Please enter valid bounds")
            continue
        else:
            break
        
    for i in range(lx1, ux1 + 1):
        y = (m1 * i) + b1
        yvalues.append(y)

main()
print(yvalues)
print("*" * 75)