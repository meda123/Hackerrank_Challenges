# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

'''
Input:
6 4
give me one grand today night (magazine)
give one grand today (note)

Output:
Yes

Note - case sensitive as well
'''

import math
import os
import random
import re
import sys

####### SOLUTION #1: USING COUNTER #########

from collections import Counter

def checkMagazine(magazine, note):
    answer = (Counter(note) - Counter(magazine)) == {}

    if answer:
        print "Yes"
        return
    else:
        print "No"
        return

####### SOLUTION #2: MANUAL METHOD #########

def ransom_note(magazine, note):
    magazine_dictionary = {}

    # Create a dictionary with words on the magazine and put the number
    # of ocurrences in the value

    for m in magazine:
        print m
        if magazine_dictionary.get(m) != None:
            if(magazine_dictionary[m] > 0):
                magazine_dictionary[m] += 1
        else:
            magazine_dictionary[m] = 1

    # Loop through each word in the ransom note and see if it is present in the
    # magazine_dictionary, if so remove word from the dictionary and continue
    # the loop. Otherwise, exit the function because word was not found

    for n in note:
        if magazine_dictionary.get(n) is None or magazine_dictionary[n] == 0:
            print "No"
            return
        else:
            print magazine_dictionary[n]
            magazine_dictionary[n] -= 1

        print "Yes"
        return
