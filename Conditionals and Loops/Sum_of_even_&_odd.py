n = int(input())
odd = 0
even = 0

while n > 0:
    r = n % 10
    if r % 2 == 0:
        even += r
        n = n//10
    else:
        odd += r
        n = n//10
    r += 1
print(even, odd)
