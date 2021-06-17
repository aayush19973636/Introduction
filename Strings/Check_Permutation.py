from sys import stdin


def isPermutation(string1, string2):
	#Your code goes here
    n = len(string1)
    m = len(string2)

    if n != m:
        return False

    a = sorted(string1)
    string1 = ''.join(a)

    b = sorted(string2)
    string2 = ''.join(b)

    for i in range(0,n):
        if string1[i] != string2[i]:
            return False
    return True

    #main
string1 = stdin.readline().strip()
string2 = stdin.readline().strip()

ans = isPermutation(string1, string2)

if ans:
    print('true')
else:
    print('false')
