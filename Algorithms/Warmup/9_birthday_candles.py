"""
Challenge details: https://www.hackerrank.com/challenges/birthday-cake-candles

Colleen is turning n years old! Therefore, she has n candles of various heights 
on her cake, and candle,i, has height,i,.Because the taller candles tower over 
the shorter ones, Colleen can only blow out the tallest candles.

Given the height for each individual candle, find and print the number of 
candles she can successfully blow out 

The first line contains a single integer, n, denoting the number of candles on 
the cake. 

The second line contains n space-separated integers, where each integer i 
describes the height of candle i.

Input:
4
3 2 1 3

Output: 
2

Print the number of candles Colleen blows out on a new line.

"""

def birthdayCakeCandles(n, ar):
    # Complete this function


n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)



