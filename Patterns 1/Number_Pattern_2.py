n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        if i == 1 and j == i:
            print(1, end='')
        elif j == 1:
            print(j+i-2, end='')
        elif j == i:
            print(j-1, end='')
        else:
            print(0, end='')
        j = j + 1
    print()
    i = i + 1
