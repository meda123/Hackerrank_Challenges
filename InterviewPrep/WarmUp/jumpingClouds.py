
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

import math
import os
import random
import re
import sys

def jumpingOnClouds(c):



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
