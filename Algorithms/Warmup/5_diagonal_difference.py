"""
Challenge details: https://www.hackerrank.com/challenges/diagonal-difference?h_r=next-challenge&h_v=zen

Given a square matrix of size N * N, calculate the abs difference between the
sum of it's diagonals. 

Input:
The first line contains a single integer, N.
The next N lines denotes the matrix's rows, with each line containing 
N-space separated integers describing the columns  

Input:
3
11 2 4 
4 5 6 
10 8 -12 

Output:
15 

Explation: 
    Primary diagonal is 11, 5, -12 = 4 
    Secondary diagonal is 4, 5, 10 = 19 
    Difference |4-19| = 15     

"""

#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
