n = int(input())
firstHalf = (n+1)//2
secondHalf = n//2

i = 1

while i<= firstHalf:
    spaces = 1
    while spaces <= i-1:
        print(" ", end= "")
        spaces += 1
    
    stars = 1
    while stars <= i:
        print('*', end=" ")
        stars += 1
    print()
    i +=1

i = secondHalf
while i >= 1:
    spaces = 1
    while spaces <= i-1:
        print(" ", end="")
        spaces += 1
    stars = 1
    while stars <= i:
        print('*', end=" ")
        stars += 1
    print()
    i -= 1
