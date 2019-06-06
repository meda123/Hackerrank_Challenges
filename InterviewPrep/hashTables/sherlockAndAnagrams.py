# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
'''
Anagrams: Two strings are anagrams of each other if the letter of one string can
be arranged to form the other string. Given a string, find the number of pairs of
substrings of the string that are anagrams of each other

S = mom
[m,m]
[mo,om]

INPUT:
q = number of queries
s = string to analyze

OUTPUT:
For each query, return the number of unordered anagrammic pairs

EXAMPLE 1:
2
abba
abcd

4
0
'''

import math
import os
import random
import re
import sys

def sherlockAndAnagrams(s):
    n = len(s)
    res = 0
    for l in range(1, n):
        cnt = {}
        for i in range(n - l + 1):
            subs = list(s[i:i + l])
            subs.sort()
            subs = ''.join(subs)
            if subs in cnt:
                cnt[subs] += 1
            else:
                cnt[subs] = 1
            res += cnt[subs] - 1
    print(res)


# PSEUDOCODE
'''
abba

[a,a]
[b,b]
[ab,ba]
[abb,bba]

Information:


''''
