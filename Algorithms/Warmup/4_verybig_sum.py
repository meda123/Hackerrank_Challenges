"""
Challenge details: https://www.hackerrank.com/challenges/a-very-big-sum

"""

#!/bin/python

import sys

def aVeryBigSum(n, ar):
    total = sum(ar)
    return total
 
"""
Explanation: Sum items inside the ar list and n is the lenght of list. I think
that in other archaic programming language, this would test memory allocation
since we summing a list of large numbers. Python list (ar) is dynamic so it 
takes care of on it's own. 

"""

# Provided by Hackerrank     
n = int(raw_input().strip())
ar = map(long, raw_input().strip().split(' '))
result = aVeryBigSum(n, ar)
print(result)


