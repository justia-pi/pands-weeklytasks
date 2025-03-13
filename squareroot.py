# Program that takes a positive floating-point number as input and outputs an approximation of its square root.
# Author: Justyna Pinkowska



def round_to_one_decimal(number): # Rounds a float to one decimal place
    return round(number, 1)

n = float(input("Please enter a positive number: "))
def sqrt(n):
    
<<<<<<< HEAD
    approximate = n/2
    new_approximate = (approximate + n/approximate)/2
    while new_approximate != approximate:
        approximate = new_approximate
        new_approximate = (approximate + n/approximate)/2
    return approximate
=======
    approx = n/2
    next_approx = (approx + n/approx)/2
    while next_approx != approx:
        approx = next_approx
        next_approx = (approx + n/approx)/2
    return approx
>>>>>>> b4bc0eaec7bb35d43213ff158a45d1589257419d

x = round_to_one_decimal(sqrt(n))
print(f"The square root of {n} is approx. {x}.")
