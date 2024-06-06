#!/usr/bin/env python3

# Author Name: Prasad Mistry
# Author ID: pmistry21@myseneca.ca

# Description: This program will improve on lab4a.py 
# by performing the same joins, match, and diffs on lists.

def join_lists(l1, l2):
    # Join_lists will return a list that contains every value from both l1 and l2.
    return list(set(l1)|set(l2))

def match_lists(l1, l2):
# Match_lists will return a list that contains all values found in both l1 and l2.
    return list(set(l1)&set(l2))

def diff_lists(l1, l2):
    # Diff_lists will return a list that contains all different values, which are not shared between the lists.
    return list(set(l1)^set(l2))

# Main program.
if __name__ == '__main__':
    list1 = list(range(1,10))
    list2 = list(range(5,15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))