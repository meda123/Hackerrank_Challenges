
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
