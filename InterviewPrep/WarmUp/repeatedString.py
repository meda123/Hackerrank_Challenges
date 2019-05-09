
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
    
    noOfa = 0
    for i in s:
        if i == 'a':
            noOfa  += 1
    res = noOfa  * (n / len(s))
    for i in s[:n % len(s)]:
        if i == 'a':
            res += 1
    return res
