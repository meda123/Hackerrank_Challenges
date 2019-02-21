
# Challege: https://www.hackerrank.com/challenges/nested-list/problem

allStudents = []

for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())

    allStudents.append([name,score])

#sort nested list with student names
allStudents.sort(key = lambda x:x[1])


#Grab the two students with the second lowest scores
twoLowest= [allStudents[1], allStudents[2]]


print twoLowest


# Need to get the second lowest scores first
# Keep the names of the students associated with those names too

# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

#OTHER APPROACH 

from collections import OrderedDict

n=int(raw_input())
ar={}
val_ar=[]
for i in range(0,n):
    tmp_name=raw_input()
    tmp_marks=float(raw_input())
    ar[tmp_name]=tmp_marks
    val_ar.append(tmp_marks)

set_val=set(val_ar)
val_ar=list(set_val)
val_ar.sort()
sec_mark=val_ar[1]
##print sec_mark
final_ar=[]
for i in ar:
    if(sec_mark==ar[i]):
        final_ar.append(i)

final_ar.sort()
for i in final_ar:
    print i
