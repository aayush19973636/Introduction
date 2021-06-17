n = int(input())
totalSpace = (n*2)-2
i = 1

while i <= n:
    j = 1
    while j <= i:
        print(j, end='')
        j += 1
    space = 1
    while space <= totalSpace:
        print(" ", end="")
        space += 1
    totalSpace -= 2
    j = i
    while j > 0:
        print(j, end="")
        j -= 1
    print()
    i += 1
