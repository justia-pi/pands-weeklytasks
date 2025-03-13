# Program that takes a positive floating-point number as input and outputs an approximation of its square root.
# Author: Justyna Pinkowska



def round_to_one_decimal(number): # Rounds a float to one decimal place
    return round(number, 1)

n = float(input("Please enter a positive number: "))
def squareRoot(n):
    
    approximate = n/2
    new_approximate = (approximate + n/approximate)/2
    while new_approximate != approximate:
        approximate = new_approximate
        new_approximate = (approximate + n/approximate)/2
    return approximate

x = round_to_one_decimal(squareRoot(n))
print(f"The square root of {n} is aprox. {x}.")