# https://www.hackerrank.com/challenges/capitalize/problem
'''
Sample input:
chris alan

Sample output:
Chris Alan

'''

input = raw_input()
test = input.split()
test2 = []
for i in test:
    n = i.capitalize()
    test2.append(n)

print(' '.join(test2))

#print test2


# if __name__ == '__main__':
#     ptr = open(os.environ['OUTPUT_PATH'], 'w')
#     s = raw_input()
#     result = solve(s)
#     fptr.write(result + '\n')
#     fptr.close()
