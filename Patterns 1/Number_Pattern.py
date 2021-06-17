n = int(input())
i = 0
while i <= n:
    j = 1
    temp = 1
    while j <= n - i:
        print(temp, end='')
        j = j + 1
        temp = temp + 1
    print()
    i = i + 1
