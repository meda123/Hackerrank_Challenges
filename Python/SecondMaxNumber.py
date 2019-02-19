
# Challenge: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


# My solution
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    uniqueArr = list(set(arr))
    uniqueArr.sort()
    print(uniqueArr[(len(uniqueArr) - 2)])
