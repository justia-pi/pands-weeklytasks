# Program allows  user to input any positive integer and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Ends if the current value is one. 
# Author: Justyna Pinkowska

positive_integer = int(input("Input any positive integer:"))
print(positive_integer, end=" ")

while positive_integer != 1:   

    if positive_integer % 2 == 0: # checks if a given positive_integer is even
        positive_integer = int(positive_integer / 2)
        
    else:
        positive_integer = int(positive_integer * 3 + 1)
    print(positive_integer, end=" ")


     

print() # prints space after each number instead of new line

