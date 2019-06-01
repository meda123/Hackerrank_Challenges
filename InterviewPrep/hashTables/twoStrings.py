#https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

'''
Input:
2
hello
world
hi
world

Output:
YES
NO
'''

from collections import Counter
# Complete the twoStrings function below.
def twoStrings(s1, s2):
    #cases = raw_input()
    #print cases

    #i = j = 0
    #while(i<len(a) and j<len(b)):
    dict_word1 = Counter(s1)
    dict_word2 = Counter(s2)

    for key in dict_word1.keys():
        if key in dict_word2.keys():
            print "YES"
            return
    print "NO"
    #return



'''
#PSEUDOCODE
# Int
# List
'''
