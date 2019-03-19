
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

'''
SAMPLE INPUT:
5
2 3 6 6 5

SAMPLE OUTPUT:
5

EXPLANATION
Given list iS [2,3,6,6,5] The maximum score is 6, second maximum is 5 .
Hence, we print  as the runner-up score.
'''

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    uniqueArr = list(set(arr))
    uniqueArr.sort()
    print(uniqueArr[(len(uniqueArr)-2)])
    print (uniqueArr[:-1])
