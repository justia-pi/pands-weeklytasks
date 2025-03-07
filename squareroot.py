# Program that takes a positive floating-point number as input and outputs an approximation of its square root.
# Author: Justyna Pinkowska



def round_to_one_decimal(number): # Rounds a float to one decimal place
    return round(number, 1)

n = float(input("Please enter a positive number: "))
def sqrt(n):
    
    approx = n/2
    next_approx = (approx + n/approx)/2
    while next_approx != approx:
        approx = next approx
        next_approx = (approx + n/approx)/2
    return approx

x = round_to_one_decimal(sqrt(n))
print(f"The square root of {n} is approx. {x}.")
