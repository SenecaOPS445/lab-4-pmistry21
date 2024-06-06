#!/usr/bin/env python3

# Author Name: Prasad Mistry
# Author ID: pmistry21@myseneca.ca

# Description: This program will output strings (first five, etc.).

#Strings 1.
str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(str1):
    # Gets the first five strings.
    return str1[:5]

def last_seven(str1):
    # Gets the last seven strings.
    return str1[-7:]

def middle_number(str1):
    # Gets the middle number.
    str1 = str(str1)
    return str1[1] + str1[2]

def first_three_last_three(str1, str2):
    # Gets the first and last three strings.
    str1 = str(str1)
    str2 = str(str2)
    return str1[:3] + str2[-3:]

# Main program.
if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))