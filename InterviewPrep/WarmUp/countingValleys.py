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



    #logic: loop through n
    # look for consecutive UU, count that as one valley

    count = 0
    i = 0

    while i<(n-1):
        if s[i] == "U"
        
