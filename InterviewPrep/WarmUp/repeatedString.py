
# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup


import math
import os
import random
import re
import sys


# aba
# Make it to length 10
# loop through extended string and find 'a'


#aba
#aba aba aba a


def repeatedString(s, n):

    # tracks frequency of "a" character in s string
    ocurrenceOfCharInString = 0

    for i in s:
        if i == 'a':
            ocurrenceOfCharInString += 1

    # frequency of "a" if string was "n" length (withOUT residual (3))
    totalOccurrenceOfChar = ocurrenceOfCharInString * (n / len(s))

    #loop through residual text, for i in s[:1]
    for i in s[:n % len(s)]:
        if i == 'a':
            totalOccurrenceOfChar += 1
            
    return totalOccurrenceOfChar
