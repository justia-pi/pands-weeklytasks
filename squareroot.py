# Program that takes a positive floating-point number as input and outputs an approximation of its square root.
# Author: Justyna Pinkowska
# The Babylonian method

def round_to_one_decimal(number): # Rounds a float to one decimal place
    return round(number, 1)

n = float(input("Please enter a positive number: "))
def sqrt(n):
   if n < 0:
        raise ValueError("Cannot calculate the square root of a negative number")
    if n == 0:
        return 0 
    
    approx = n/2 # initial guess for the square root of n
    next_approx = (approx + n/approx)/2  # calculates approximation by averaging the current guess (approx) with n divided by the current guess
    while next_approx != approx:  #  will continue to execute as long as the new_approximate calculated in the previous step is not equal to the approximate
        approx = next_approx
        next_approx = (approx + n/approx)/2 # recalculates a new napprox using the updated approx, repeats until the condition in the while loop becomes false
    return approx


x = round_to_one_decimal(sqrt(n))
print(f"The square root of {n} is approx. {x}.")
