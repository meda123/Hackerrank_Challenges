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

################ SOLUTION #1 ################
from collections import Counter
# Complete the twoStrings function below.
def twoStrings(s1, s2):

    #Convert each string into a dictionary
    dict_word1 = Counter(s1)
    dict_word2 = Counter(s2)

    #Check if the key in first dictionary is in second
    for key in dict_word1.keys():
        if key in dict_word2.keys():
            return "YES"

    #If no matches found print "NO"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s1 = raw_input()

        s2 = raw_input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()


################ SOLUTION #2 ################

def solve(a,b):
    a = ''.join(sorted(a))
    b = ''.join(sorted(b))
    #print a
    #print b
    i = j = 0
    while(i<len(a) and j<len(b)):
        if(a[i]==b[j]):
            return "YES"
        elif(a[i]<b[j]):
            i+=1
        else:
            j+=1
    return "NO"

if __name__ == "__main__":
    cases = int(input())
    results = []
    for case in range(cases):
        a = raw_input()
        b = raw_input()
        results.append(solve(a,b))
    for result in results:
        print result
