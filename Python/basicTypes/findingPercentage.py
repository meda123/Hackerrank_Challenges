
#https://www.hackerrank.com/challenges/finding-the-percentage/problem

'''
Sample input:
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh

Sample output:
26.50
'''


################################## FIRST APPROACH ###########################

#Grab first integer
name=int(input())

#Blank array to store student grades
ar={}

#Entering name/score loop
for i in range(0,n):

    #Capture first line
    s=input()

    #Split name and score based on name
    ss=s.split(" ")

    #name
    name=ss[0]

    #scores
    m1=float(ss[1])
    m2=float(ss[2])
    m3=float(ss[3])

    m_avg=(m1+m2+m3)/3.0

    #Add name with average score (including format)
    ar[name]="%.2f" % m_avg

#Capture the last line (name for which average must be printed)
s_name=input()

print(ar[s_name])



################################## SECOND APPROACH ###########################

if __name__ == '__main__':

    n = int(raw_input())

    student_marks = {}

    for i in range(0,n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        average_scores = (scores[0] + scores[1] + scores[2]) / 3.0

        student_marks[name] = "%.2f" % average_scores

    query_name = raw_input()

    print student_marks[query_name]
