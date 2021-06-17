n = int(input())
firstHalf = (n+1)//2
secondHalf = (n//2)

for i in range(1,firstHalf+1):
    for j in range(1, firstHalf-i+1):
        print(" ", end="")
    for j in range(1,2*i):
        print('*', end="")
    print()

for i in range(secondHalf,0,-1):
    for j in range(secondHalf-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        print('*', end="")
    print()
