# https://www.hackerrank.com/challenges/python-string-split-and-join/problem

'''
SAMPLE INPUT
this is a string

SAMPLE OUTPUT
this-is-a-string
'''

def split_and_join(line):
    string_list = line.split(" ")
    joined_list = "-".join(string_list)
    return joined_list


if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result
