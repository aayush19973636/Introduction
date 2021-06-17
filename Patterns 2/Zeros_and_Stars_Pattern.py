n = int(input())

i = 1
j = 1
while i <= n:
    j = 1
    while j<=n:
        if i==j:
            print('*', end="")
        else:
            print('0', end="")
        j += 1
    j -= 1
    print('*', end="")

    while j>0:
        if i==j:
            print('*', end="")
        else:
            print('0', end="")
        j -= 1
    print()
    i+=1