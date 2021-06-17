def printTable(start, end, step):
    current = start
    
    while current <= end:
        c = (current-32)*5/9
        print(current, int(c))
        current += step


s = int(input())
e = int(input())
step = int(input())
printTable(s, e, step)
