# This program reads in any lenght character account number and outputs the account number with only the last 4 digits showing (and the rest of digits is replaced with Xs)
# Author Justyna Pinkowska

# User imput of the account number.
accountno = input("Please enter your account number: ")

# Substracts 4 from the total lenght of the accountno, the rest masks with Xs.
print(f"X" * (len(accountno) - 4) + str(accountno[-4:]))

