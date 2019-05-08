# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup


import math
import os
import random
import re
import sys

def countingValleys(n,s):
    # n number of steps
    # s = string given to us
    # valley is represented by two consecutive UU

    level = 0
    valley = 0

    for i in range(n):
        if(s[i]=='U'):
            level = level + 1
            if (level == 0):
                valley = valley + 1
        else
            level = level - 1

    return valley


    #logic: loop through n
    # look for consecutive UU, count that as one valley
