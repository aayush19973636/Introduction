def sumUnique(li):
    s = set()
    
    for i in li:
        s.add(i)
    sum = 0
    for i in s:
        sum += i
    return sum

print(sumUnique([1,2,3,4,5,6,7,1,2,3]))
