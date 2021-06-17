from sys import stdin


def removeAllOccurrencesOfChar(string, ch):
	# Your code goes here
    counts = string.count(ch)

    string = list(string)

    while counts:
        string.remove(ch)
        counts -= 1
    
    string = "".join(string)
    return string



    #main
string = stdin.readline().strip()
ch = stdin.readline().strip()[0]

ans = removeAllOccurrencesOfChar(string, ch)

print(ans)
