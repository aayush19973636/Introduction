n = int(input())
i = 1

while i <= n:
    spaces = 1
    while spaces <= n-i:
        print(" ", end="")
        spaces += 1
    p = 1
    j = 1
    while j <= i:
        print('*', end="")
        p += 1
        j += 1
    p = i-1
    while p >= 1:
        print('*', end="")
        p = p-1
    print()
    i += 1
