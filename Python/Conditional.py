import sys


N = int(raw_input().strip())

if N % 2 == 0:
    if N >= 2 and N <=5:
        #print "Not weird"
        sys.stdout.write("Not weird")
    elif N >= 6 and N <=20:
        #print "Weird"
        sys.stdout.write("Weird")
    elif N > 20:
        #print "Not Weird"
        sys.stdout.write("Not Weird")

if N % 2 == 1:

#else:
    #print "Weird"
    sys.stdout.write("Weird")



if N % 2 == 1:
    #print(w)
    sys.stdout.write("Weird")
elif N % 2 == 0 and (N>=2 and N<5):
    #print(nw)
    sys.stdout.write("Not weird")
elif N % 2 == 0 and (N>=6 and N<=20):
    #print(w)
    sys.stdout.write("Weird")
elif N % 2 == 0 and (N>20):
    #print(nw)
    sys.stdout.write("Not weird")
