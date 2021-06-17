
from sys import stdin


def reverseEachWord(string):
	# Your code goes here
    words = string.split(" ")
    newWords = [word[::-1] for word in words]

    newString = " ".join(newWords)
    return newString


    #main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)
