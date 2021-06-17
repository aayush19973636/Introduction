n = int(input())

if n <= 0:
    print(False)
else:
    sum = 0

    while n > 0:
        sum = sum + n
        n -= 1
    print(sum)
