#Bank currency
#Prompt the user and read in two money amounts (in cent)
#Add the two amounts
#Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount
#Justyna Pinkowska

amount1 = 65  # in cent
amount2 = 180 # in cent
x = (amount1 + amount2)/ 100 # converts the total amount from cents to euros
txt = f"The sum of these is €{x}"  # uses an f-string to create a string
print(txt)
 
