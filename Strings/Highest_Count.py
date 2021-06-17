import sys
from sys import stdin


def highestOccuringChar(string):
	#Your code goes here
    freq = {}

    for i in string:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    res= max(freq, key = freq.get)
    return res


    #main
string = stdin.readline().strip()
ans = highestOccuringChar(string)

print(ans)
