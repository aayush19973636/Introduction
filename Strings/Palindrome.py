
from sys import stdin


def isPalindrome(string):
	# Your code goes here
    return str(string) == str(string)[::-1]


    #main
string = stdin.readline().strip()
ans = isPalindrome(string)

if ans:
    print('true')
else:
    print('false')
