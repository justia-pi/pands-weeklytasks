# This program reads in any lenght character account number and outputs the account number with only the last 4 digits showing (and the rest of digits is replaced with Xs)
# Author Justyna Pinkowska

accountno = input("Please enter your account number: ")

print(f"X" * (len(accountno) - 4) + str(accountno[-4:]))

