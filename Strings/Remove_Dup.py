from sys import stdin


def removeConsecutiveDuplicates(string):
    seen = string[0]
    ans = string[0]

    for i in string[1:]:
        if i != seen:
            ans += i
            seen = i
    return ans


    #main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)
