# https://www.hackerrank.com/domains/python?filters%5Bstatus%5D%5B%5D=unsolved&filters%5Bsubdomains%5D%5B%5D=py-strings&badge_type=python

'''
Given a string "S" and width "w"
Task is to wrap the string into a paragraph of width w

Input:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Output:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''

import textwrap

def wrap(string, width_max):
    return textwrap.fill(string, max_width)
