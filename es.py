# Program reads in a .txt file and outputs no of e's (regardless of case) it contains. 
# The program takes a filename from an argumment on the command line.
# If no filename provided, itthe program prints a message and exits.
# If the provided file does not exist or it is not a .txt file, the program prints an error message and exits.
# Author: Justyna Pinkowska

import os
import sys


def filenames():
    if len(sys.argv) != 2:                                  # checks if filename provided
        print("Please provide a txt file as an argument.")
        sys.exit()                                          # exits the program

    FILENAME = sys.argv[1]


    if not os.path.isfile(FILENAME):                        # checks if file exists
        print("File does not exist")

    elif not FILENAME.lower().endswith(".txt"):             # checks if file is a txt file
        print("You need to provide a .txt file")



    else:
        with open(FILENAME, "r") as f:                      # Reads the file
            content = f.read().lower()                      # Converts string to lowercase
            num = content.count('e')                        # Counts on e's , returns int
        
            print(num)
filenames()






