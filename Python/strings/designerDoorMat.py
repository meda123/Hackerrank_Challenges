# https://www.hackerrank.com/challenges/designer-door-mat/problem

'''
Input format:
A single line containing the space separated values of N and M

Output:
Output the design pattern

'''

import sys

n, m = map(int, raw_input().split())
pattern = [('.|.' * (2 * i + 1)).center(m, '-') for i in range(n // 2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
