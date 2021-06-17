n = int(input())

for i in range(1, n+1):
    temp = n
    for j in range(1,i):
        print(temp, end="")
        temp -=1
    for j in range(1, (2*n) - (2*i) + 2):
        print(n-i+1, end="")
    for j in range(1,i):
        temp += 1
        print(temp, end="")        
    print()
    
for i in range(n-1,0,-1):
    temp = n
    for j in range(1,i):
        print(temp, end="")
        temp -=1
    for j in range(1, (2*n) - (2*i) + 2):
        print(n-i+1, end="")
    for j in range(1,i):
        temp += 1
        print(temp, end="")        
    print()
