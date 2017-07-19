"""
Details: https://www.hackerrank.com/contests/moodysuniversityhackathon/challenges/learning-from-the-past

Input:
2
1 2 3
3 3 0

Output: 
6 

Explanation: 
There are n = 2 days to analyze (two days)
Max profit first day would be 2+3 = 5 
Max profit second day would be 3+3 = 6

Out of those two (5 & 6), the highest would be the second day. Print 6. 

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys 

# Read in number of days for which to calculate best possible trades 
n = int(raw_input().strip())

# Read in each line of potential trades 
pot_trades = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    pot_trades.append(a_temp)

# Step 1: Sort inside list, return max items in each day (top 2)
max_trade = []
for i in range(n):
    test = sorted(pot_trades[i]) 
    max_two = sum(test[-2:])
    max_trade.append(max_two)
    
# Step 2:Once the max trade for each day is calculated, pick highest trade out of n days 
print max(max_trade)
