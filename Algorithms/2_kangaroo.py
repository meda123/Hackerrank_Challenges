"""
Challenge details: https://www.hackerrank.com/challenges/kangaroo

Figure if two Kangaroos, who start in different places and jump at different
speed (towards positive infinity) will land at the same location with the same
number of jumps.

Test cases:

Input: 0 3 4 2
Output: Yes 

The two kangaroos jump through the following sequence of locations:
0 - 3 - 6 - 9 - 12
4 - 6 - 8 - 10 - 12  

Input: 0 2 5 3
Output: No 

"""

#!/bin/python

import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
     if (v1 > v2) and ((x1 - x2) % (v1 - v2)) == 0:
       return"YES"
    else:
       return"NO"

x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)