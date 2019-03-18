
#https://www.hackerrank.com/challenges/python-lists/problem

'''
Input:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Output:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

'''

if __name__ == '__main__':

    list = []
    N = int(raw_input())

    while N > 0:
        i = raw_input.split()

        #insert usually comes with two digits 
        if i[0] == "insert":
            list.insert(int(i[1])), int(i[2]))

        elif i[0] == "remove":
            list.remove(int(i[1]))

        elif i[0] == "append":
            list.append(int(i[1]))

        elif i[0] == "sort":
            list.sort()

        elif i[0] == "reverse":
            list.reverse()

        elif i[0] == "pop":
            list.pop()

        elif i[0] == "print"
            print(list)

        N -=1
