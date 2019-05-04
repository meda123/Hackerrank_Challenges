# link: https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    count = 0
    ar.sort()
    i = 0

    while i<(n-1):
        if ar[i] == ar[i+1]:
            count = count+1
            i+=2
        else:
            i+=1
    return count


'''
The count variable tracks the number of "matched socks"

Loop through each item in the list, compare the first and second item. If the
items match, add to count, otherwise increase (i) only once to compare the second
and third item.

return count at the very end

'''
