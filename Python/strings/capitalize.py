# https://www.hackerrank.com/challenges/capitalize/problem
'''
Sample input:
chris alan

Sample output:
Chris Alan

'''
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    full_name = s.split(' ')
    return ' '.join((word.capitalize() for word in full_name))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = raw_input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
