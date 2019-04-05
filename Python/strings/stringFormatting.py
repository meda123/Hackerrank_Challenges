# https://www.hackerrank.com/challenges/python-string-formatting/problem

'''
INPUT:
A single integer denoting n

OUTPUT:
Print n lines where each line i contains the respective decimal, octal,
capitalized hexadecimal, and binary values for i.
Each printed value must be formatted to the width of the binary value n.

'''


def print_formatted(number):
    width = len(bin(number)) - 2

    for n in range(1, number+1):
        line = '{1: >{0}d} {1: >{0}o} {1: >{0}X} {1: >{0}b}'.format(width, n)
        print line


if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)
