import sys
from sys import stdin


def getCompressedString(string):
	# Your code goes here
    i = 0
    x = ''

    while i < len(string):
        j = i + 1
        c = 1
        while j < len(string) and string[i] == string[j]: # For mismatch
               j += 1
               c+=1
        if c==1:
            x+=string[i]
        else:
            x+=string[i]+str(c)
        i = j
    return x



    #main
string = stdin.readline().strip()
ans = getCompressedString(string)

print(ans)
