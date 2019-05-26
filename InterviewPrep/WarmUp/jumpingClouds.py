
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

import math
import os
import random
import re
import sys

def jumpingOnClouds(c):

n = len(c)

min = 0
i = 0

while i < n-1:
    #Check that next +2 position is still within list AND if moving +2 is of value '0' in the list
    if i+2 < n and c[i+2] == 0:
        # If moving 2, move index to +2 in the list
        i = i + 2
        #increase minimum steps counter
        min = min + 1
    else
        # Can only move to the next step
        i = i+ 1
        #Increase minimum steps counter
        min = min + 1

#Return counter  
return min






# EXPLANATION
'''
Given = [0, 0, 1, 0, 0, 1, 0]
Rules:
- Can jump +1 and +2
- Avoid 1
- Return the minimum number of jumps required
'''

# PSEUDOCODE
'''
loop through list
    #for each number check
        if +2 option is 0
            jump
        otherwise
            jump only +1
''''
