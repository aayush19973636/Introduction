n = int(input())

for i in range(1, n+1):
    count = 1
    for j in range(1, i):
        print(" ", end="")
        count += 1
    num = i
    for j in range(count, n+1):
        print(num, end="")
        num += 1
    print()

for i in range(n-1, 0, -1):
    count = 1
    for j in range(1, i):
        print(" ", end="")
        count += 1
    num = i
    for j in range(count, n+1):
        print(num, end="")
        num += 1
    print()
