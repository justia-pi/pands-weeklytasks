# This program reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs)
# Author Justyna Pinkowska

accountno = input("Please enter your account number: ")
# Using slicing, starts Xs from the fourth character from the end of the string
print(f"XXXXXX" + str(accountno[-4:]))

