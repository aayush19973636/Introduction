n = int(input())
start = 1

for i in range(1, n+1):
    for j in range(start, start+n):
        print(j, end=" ")
    print()
    
    if i == (n+1)//2:
        if n%2 != 0:
            start = n*(n-2)+1
        else:
            start = n*(n-1)+1
    elif i>(n+1)//2:
        start = start - 2*n
    else:
        start = start + 2*n


