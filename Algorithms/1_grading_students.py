"""
Challenge details: https://www.hackerrank.com/challenges/grading
Process the following list of grades and round-up according to challenge rules

Input:
4
73
67
38
33

Expected output:
75
67
40
33

"""

#!/bin/python

import sys

# Function definition provided by Hackerrank 
def solve(grades):
    # My solution
    for grade in grades:
        if grade >= 38:
            # Added the +2 to round up to the next multiple of 5 
            multiple = int(5 * round(float(grade+2)/5))
            if multiple - grade <= 2:
                print multiple
            else:
                print grade
        else:
            print grade
           
        

# Provided by Hackerrank         
n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))
