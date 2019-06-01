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


def checkMagazine(magazine, note):
    hash_words = {}

    for m_word in magazine:

        if hash_words.get(m_word) != None:
            if (hash_words[m_word] > 0):
                hash_words[m_word] += 1
        else:
            hash_words[m_word] = 1

    for r_word in note:
        if hash_words.get(r_word) is None or hash_words[r_word] == 0:
            print "No"
            return
        else:
            hash_words[r_word] -= 1

    print "Yes"
    return
    
test = checkMagazine("hello meda is", "zips")
print test


#Pseudocode
