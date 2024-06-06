#!/usr/bin/env python3

# Author Name: Prasad Mistry
# Author ID: pmistry21@myseneca.ca

# Description: This program will determine if a value is an integer or not.


# Determines if it is an integer or not.
def is_digits(sobj):
    # Place code here - loop through each character in sobj.
    for char in sobj:
        if not char.isdigit():
            return False
    else:    
        return True

# Main program (outputs whether an integer or not).
if __name__ == '__main__':
    test_list = ['x3058', '3058', '8503x', '8503']
    for item in test_list:
        if is_digits(item):
            print(item, 'is an integer.')
        else:
            print(item, 'is not an integer.')