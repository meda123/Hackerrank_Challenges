
# HR: https://www.hackerrank.com/challenges/list-comprehensions/problem
'''
Sample Input:
1
1
1
2

Sample Output:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

Cocenpt:
List comprehensions are an elegant way to build a list without having to use
different for loops to append values one by one

Explantion:
You are given three integers x,y,z representing the dimensions of a cuboid
along with an integer  N. You have to print a list of all possible coordinates
given by  on a 3D grid where the sum of  is not equal to N .

'''


x=int(raw_input())
y=int(raw_input())
z=int(raw_input())
n=int(raw_input())

print([ [i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n ])
