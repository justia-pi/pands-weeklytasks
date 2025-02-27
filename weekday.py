# Program that whether or not today is a weekday. 
# Author: Justyna Pinkowska


import datetime
today = datetime.date.today()     # gets the current date
weekday_number = today.weekday()  # returns a day of a week as int (0,6)

if 1 <= weekday_number <= 4:
      print("Yes, unfortunately today is a weekday.")
else:
       print("It is the weekend, yay!")