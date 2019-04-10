
# https://www.hackerrank.com/challenges/python-mutations/problem

'''
INPUT:
abracadabra
5 k

OUTPUT:
abracadabra
'''

s=raw_input()
in_str_ar=raw_input().strip().split()
pos=int(in_str_ar[0])
c=in_str_ar[1]
final_str=s[:pos]+c+s[pos+1:]
print final_str
